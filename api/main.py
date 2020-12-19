import models
import re
import json
import uvicorn
import pandas as pd
from datetime import datetime
from models import AccountType, IncomeTypes, InvestmentTypes, ExpenseTypes, BudgetCategories, \
  Account, Investments, Expenses, Budget, Income

from yahooquery import Ticker
from yahoofinancials import YahooFinancials
import yfinance
from sqlalchemy.orm import Session
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


class BudgetCategoriesRequest(BaseModel):
  name: str


class AccountTypeRequest(BaseModel):
  name: str
  type: str


class InvestmentTypeRequest(BaseModel):
  name: str


class ExpenseTypeRequest(BaseModel):
  name: str


class IncomeTypeRequest(BaseModel):
  name: str


class AccountRequest(BaseModel):
  name: str
  balance: float
  account_type_id: int


class ExpensesRequest(BaseModel):
  amount: float
  expense_date: datetime
  paid_to: str
  budget_entry_id: int
  account_id: int


class InvestmentsRequest(BaseModel):
  investment_type_id: int
  ticker: str
  shares: int
  price_per_share: float
  date: datetime
  investment_account_id: int


class IncomeRequest(BaseModel):
  source: str
  amount: float
  income_date: datetime
  taxes: float
  saved: float
  income_type_id: int
  account_id: int


class BudgetRequest(BaseModel):
  name: str
  amount: float
  category_id: int
  importance: str


def get_db():
  try:
    db = SessionLocal()
    yield db
  finally:
    db.close()


@app.get("/")
def home(request: Request, forward_pe=None, dividend_yield=None, ma50=None, ma200=None, db: Session = Depends(get_db)):
  """
  show all stocks in the database and button to add more
  button next to each stock to delete from database
  filters to filter this list of stocks
  button next to each to add a note or save for later
  """

  stocks = db.query(Stock)

  if forward_pe:
    stocks = stocks.filter(Stock.forward_pe < forward_pe)

  if dividend_yield:
    stocks = stocks.filter(Stock.dividend_yield > dividend_yield)

  if ma50:
    stocks = stocks.filter(Stock.price > Stock.ma50)

  if ma200:
    stocks = stocks.filter(Stock.price > Stock.ma200)

  stocks = stocks.all()

  return templates.TemplateResponse("home.html", {
    "request": request,
    "stocks": stocks,
    "dividend_yield": dividend_yield,
    "forward_pe": forward_pe,
    "ma200": ma200,
    "ma50": ma50
  })


# def fetch_stock_data(id: int):
#
#     db = SessionLocal()
#
#     stock = db.query(Stock).filter(Stock.id == id).first()
#
#     yahoo_data = yfinance.Ticker(stock.symbol)
#
#     stock.ma200 = yahoo_data.info['twoHundredDayAverage']
#     stock.ma50 = yahoo_data.info['fiftyDayAverage']
#     stock.price = yahoo_data.info['previousClose']
#     stock.forward_pe = yahoo_data.info['forwardPE']
#     stock.forward_eps = yahoo_data.info['forwardEps']
#     stock.dividend_yield = yahoo_data.info['dividendYield'] * 100
#
#     db.add(stock)
#     db.commit()

# Budget category
@app.get("/budget/category")
def budget_categories(db: Session = Depends(get_db)):
  budget_categories = db.query(BudgetCategories).all()

  return {
    "code": "success",
    "budget_categories": budget_categories
  }


@app.post("/budget/category")
def add_budget_category(budget_category_request: BudgetCategoriesRequest, db: Session = Depends(get_db)):
  category = BudgetCategories()
  category.name = budget_category_request.name

  db.add(category)
  db.commit()

  return {
    "code": "success",
    "message": "budget category was added to the database"
  }


# get all budget
@app.get("/budget")
def get_budget(db: Session = Depends(get_db)):
  entries = db.query(Budget, BudgetCategories).filter(Budget.category_id == BudgetCategories.id).all()

  reformat = []
  for entry in entries:
    new_entry = {
      'id': entry[0].id,
      'name': entry[0].name,
      'budget_amount': entry[0].amount,
      'importance': entry[0].importance,
      'category': entry[1].name
    }
    reformat.append(new_entry)

  return {
    "code": "success",
    "budget": reformat
  }


# add budget
@app.post("/budget")
def add_budget(budget_request: BudgetRequest, db: Session = Depends(get_db)):
  print(budget_request)
  budget_entry = Budget()
  budget_entry.name = budget_request.name
  budget_entry.amount = budget_request.amount
  budget_entry.category_id = budget_request.category_id
  budget_entry.importance = budget_request.importance

  db.add(budget_entry)
  db.commit()

  #     background_tasks.add_task(fetch_stock_data, stock.id)

  return {
    "code": "success",
    "message": "budget entry was added to the database"
  }


@app.get("/investment/type")
def get_investment_types(db: Session = Depends(get_db)):
  investment_types = db.query(InvestmentTypes).all()

  return {
    "code": "success",
    "investment_types": investment_types
  }


@app.post("/investment")
def add_investment_type(investment_request: InvestmentsRequest, db: Session = Depends(get_db)):
  investment = Investments()
  investment.investment_type_id = investment_request.investment_type_id
  investment.ticker = investment_request.ticker
  investment.shares = investment_request.shares
  investment.price_per_share = investment_request.price_per_share
  investment.date = investment_request.date
  investment.investment_account_id = investment_request.investment_account_id

  db.add(investment)
  db.commit()

  return {
    "code": "success",
    "message": "investment was added to the database"
  }


# Income type category
@app.get("/investment")
def get_income_types(db: Session = Depends(get_db)):
  def wavg(group):
    d = group['price_per_share']
    w = group['shares']
    return (d * w).sum() / w.sum()

  query = db.query(Investments, InvestmentTypes).filter(Investments.investment_type_id == InvestmentTypes.id)
  data = pd.read_sql(query.statement, db.bind)

  tickers = data.groupby(['name', 'ticker'])
  stocks = pd.concat([tickers.apply(wavg).reset_index(), tickers['shares'].sum().reset_index()], axis=1)
  stocks.rename(columns={0: 'cost_basis'}, inplace=True)
  stocks.rename(columns={'name': 'investment_type'}, inplace=True)
  stocks = stocks.loc[:, ~stocks.columns.duplicated()]
  stocks['total'] = stocks.shares * stocks.cost_basis
  stocks['percent'] = stocks.iloc[:, 4:].apply(lambda x: x / x.sum())

  weight = stocks[['ticker', 'percent']]
  weight = weight.loc[:, ~weight.columns.duplicated()]
  weight_json = weight.to_json(orient='split')

  stocks['json'] = stocks.to_json(orient='split')

  invalid_escape = re.compile(r'\\([1-3][0-7]{2}|[1-7][0-7]?)')  # octal digits from 1 up to FF

  def replace_with_codepoint(match):
    return chr(int(match.group(0)[1:], 8))

  def repair(brokenjson):
    return invalid_escape.sub(replace_with_codepoint, brokenjson)

  # TODO: in frontend i can use JSON.parse
  clean_json = json.loads(repair(stocks['json'][0]))['data']
  result = []
  print(clean_json)
  for stock in clean_json:
    ticker = stock[1]
    cost_basis = round(stock[2], 2)
    shares = stock[3]
    total_value = stock[4]
    alloc = int(stock[5] * 100)

    res = {
      'investment_type': stock[0],  # join
      'ticker': ticker,  # group by
      'shares': shares,  # sum total
      'cost_basis': cost_basis,  # weighted
      'total_value': total_value,
      'actual_allocation': alloc,  # total portfolio / (price_per_share)
      'value_per_share': None,  # get from y finance
      'value_change': None,  # yfinance
      'est_total_quarter_dividend': None,  # yfinance
    }

    # TODO: Extract to function
    try:
      fin = Ticker(ticker).summary_detail[ticker]
    except:
      # print("Ticker not found", ticker)
      pass

    try:
      # This is returning a tuple in Json for some reason but not here
      vps = round(float(fin['previousClose']), 2)
      vc = round(float((fin['previousClose']) - float(cost_basis)) / 100, 2)
    except:
      # print("no PrevClose", ticker)
      pass
    try:
      etd = round(float(fin['dividendRate']) * int(shares), 2)
    except:
      # print("no div", ticker)
      pass
    try:
      pyd = round(float(fin['trailingAnnualDividendRate']), 2)
    except:
      pass
      # print("no prev Div", ticker)

    if not isinstance(fin, str):
      res['value_per_share'] = vps,
      res['est_total_quarter_dividend'] = etd,
      res['value_change'] = vc,
      res['prev_year_dividend'] = pyd,

    result.append(res)

  return {
    "code": "success",
    "investments": result,
    "doughnut": json.loads(repair(weight_json))['data']
  }


@app.post("/investment/type")
def add_investment_type(investment_type_request: InvestmentTypeRequest, db: Session = Depends(get_db)):
  investment_type = InvestmentTypes()
  investment_type.name = investment_type_request.name

  db.add(investment_type)
  db.commit()

  return {
    "code": "success",
    "message": "investment type was added to the database"
  }


# Income type category
@app.get("/income/type")
def get_income_types(db: Session = Depends(get_db)):
  income_types = db.query(IncomeTypes).all()

  return {
    "code": "success",
    "income_types": income_types
  }


@app.post("/income/type")
def add_income_type(income_type_request: IncomeTypeRequest, db: Session = Depends(get_db)):
  income_type = IncomeTypes()
  income_type.name = income_type_request.name

  db.add(income_type)
  db.commit()

  #     background_tasks.add_task(fetch_stock_data, stock.id)

  return {
    "code": "success",
    "message": "income type was added to the database"
  }


# Add Income
@app.get("/income")
def get_all_incomes(db: Session = Depends(get_db)):
  incomes = db.query(Income, IncomeTypes, Account).filter(Income.income_type_id == IncomeTypes.id).filter(
    Income.account_id == Account.id).all()

  clean_incomes = []
  for income in incomes:
    clean_incomes.append({
      'isActive': False,
      '_showDetails': False,
      'type': income[1].name,
      'account_name': income[2].name,
      'source': income[0].source,
      'amount': income[0].amount,
      'date': income[0].income_date
    })

  return {
    "code": "success",
    "incomes": clean_incomes
  }


# get all incomes
@app.post("/income")
def add_income(income_request: IncomeRequest, db: Session = Depends(get_db)):
  income = Income()
  income.source = income_request.source
  income.amount = income_request.amount
  income.income_date = income_request.income_date
  income.taxes = income_request.taxes
  income.saved = income_request.saved
  income.income_type_id = income_request.income_type_id
  income.account_id = income_request.account_id

  db.add(income)
  db.commit()

  #     background_tasks.add_task(fetch_stock_data, stock.id)

  return {
    "code": "success",
    "message": "income was added to the database"
  }


# Add Expense -> change this to budget types or none
@app.get("/budget/expense")
def get_all_expenses(db: Session = Depends(get_db)):
  expenses = db.query(Expenses, Account.name, Budget.name).all()

  clean_expenses = []
  for expense in expenses:
    clean_expenses.append({
      'isActive': False,
      '_showDetails': False,
      'from_account': expense[1],
      'paid_to': expense[0].paid_to,
      'expense_date': expense[0].expense_date,
      'amount': expense[0].amount,
      'budget_name': expense[2]
    })

  return {
    "code": "success",
    "expenses": clean_expenses
  }


@app.post("/budget/expense")
def add_expense(expense_request: ExpensesRequest, db: Session = Depends(get_db)):
  expense = Expenses()
  expense.amount = expense_request.amount
  expense.expense_date = expense_request.expense_date
  expense.paid_to = expense_request.paid_to
  expense.budget_entry_id = expense_request.budget_entry_id
  expense.account_id = expense_request.account_id

  db.add(expense)
  db.commit()

  #     background_tasks.add_task(fetch_stock_data, stock.id)

  return {
    "code": "success",
    "message": "expense was added to the database"
  }


@app.get("/accounts")
def get_all(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
  accounts = db.query(Account, AccountType).filter(Account.account_type_id == AccountType.id).all()

  reformat = {'assets': [], 'liabilities': []}
  for account in accounts:
    acc = {
      'id': account[0].id,
      'name': account[0].name,
      'account': account[1],
      'balance': account[0].starting_balance,
    }

    if (account[1].type == 'asset'):
      reformat['assets'].append(acc)

    if (account[1].type == 'liability'):
      reformat['liabilities'].append(acc)

  return {
    "code": "success",
    "accounts": reformat,
  }


@app.post("/accounts")
def create_account(account_request: AccountRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
  account = Account()
  account.name = account_request.name
  account.starting_balance = account_request.balance
  account.account_type_id = account_request.account_type_id

  db.add(account)
  db.commit()

  #     background_tasks.add_task(fetch_stock_data, stock.id)

  return {
    "code": "success",
    "message": "stock was added to the database"
  }


@app.get("/account_type")
async def get_all_account_types(db: Session = Depends(get_db)):
  account_type = db.query(AccountType)
  accounts = account_type.all()

  return {
    "code": "success",
    "account_types": accounts
  }


@app.post("/account_type")
async def create_account_type(account_type_request: AccountTypeRequest, background_tasks: BackgroundTasks,
                              db: Session = Depends(get_db)):
  account_type = AccountType()
  account_type.name = account_type_request.name
  account_type.type = account_type_request.type

  db.add(account_type)
  db.commit()

  return {
    "code": "success",
    "message": "Account Type was added to db"
  }


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
