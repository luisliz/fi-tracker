import models
from models import Account
import yfinance
from sqlalchemy.orm import Session
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
from pydantic import BaseModel

app = FastAPI()

origins = [
  "http://localhost:3000"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)

class AccountRequest(BaseModel):
    balance: int
    name: str
    account_name: str
    account_type: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def home(request: Request, forward_pe = None, dividend_yield = None, ma50 = None, ma200 = None, db: Session = Depends(get_db)):
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

@app.get("/accounts")
async def get_all(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    add one or more tickers to the database
    background task to use yfinance and load key statistics
    """

    account = db.query(Account)
    accounts = account.all()

    return {
        "code": "success",
        "accounts": accounts
    }

@app.post("/accounts")
async def create_account(account_request: AccountRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    add one or more tickers to the database
    background task to use yfinance and load key statistics
    """

    account = Account()
    account.name = account_request.name
    account.balance = account_request.balance
    account.account_name = account_request.account_name
    account.account_type = account_request.account_type
    db.add(account)
    db.commit()

#     background_tasks.add_task(fetch_stock_data, stock.id)

    return {
        "code": "success",
        "message": "stock was added to the database"
    }
