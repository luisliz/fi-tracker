from database import Base
from sqlalchemy import Column, ForeignKey, Numeric, Integer, String, TIMESTAMP, Enum
from sqlalchemy.orm import relationship


# -------------------------------------------------------------------------------------------------
# Type Tables
# -------------------------------------------------------------------------------------------------
class BudgetCategories(Base):
  __tablename__ = "budget_category"
  id = Column(Integer, primary_key=True)
  name = Column(String)


class InvestmentTypes(Base):
  __tablename__ = "investment_types"
  id = Column(Integer, primary_key=True)
  name = Column(String)


class ExpenseTypes(Base):
  __tablename__ = "expense_types"
  id = Column(Integer, primary_key=True)
  name = Column(String)


class IncomeTypes(Base):
  __tablename__ = "income_source"
  id = Column(Integer, primary_key=True)
  name = Column(String)


class AccountType(Base):
  __tablename__ = "account_types"
  id = Column(Integer, primary_key=True)
  name = Column(String)
  type = Column(Enum("asset", "liability", name="asset_liability_enum"))


# -------------------------------------------------------------------------------------------------
# Info Tables
# -------------------------------------------------------------------------------------------------
class Account(Base):
  __tablename__ = "account"
  id = Column(Integer, primary_key=True)
  name = Column(String)
  starting_balance = Column(Numeric(10, 2))
  account_type_id = Column(Integer, ForeignKey('account_types.id'))

  account = relationship(AccountType, backref='types')


class Investments(Base):
  __tablename__ = "investments"
  id = Column(Integer, primary_key=True)
  ticker = Column(String)
  shares = Column(Integer)
  price_per_share = Column(Numeric(10, 2))
  date = Column(TIMESTAMP)
  investment_account_id = Column(Integer, ForeignKey(Account.id))
  investment_type_id = Column(Integer, ForeignKey(InvestmentTypes.id))

  investment_account = relationship('Account', foreign_keys='Investments.investment_account_id')
  investment_type = relationship('InvestmentTypes', foreign_keys='Investments.investment_type_id')


class Income(Base):
  __tablename__ = "income"
  id = Column(Integer, primary_key=True)
  source = Column(String)
  amount = Column(Numeric(10, 2))
  income_date = Column(TIMESTAMP)
  taxes = Column(Numeric(10, 2))
  saved = Column(Numeric(10, 2))
  income_type_id = Column(Integer, ForeignKey(IncomeTypes.id))
  account_id = Column(Integer, ForeignKey(Account.id))
  # saved_account_id = Column(Integer, ForeignKey(AccountType.id))

  account = relationship('Account', foreign_keys='Income.account_id')
  income_type = relationship('IncomeTypes', foreign_keys='Income.income_type_id')
  # saved_account = relationship('IncomeTypes', foreign_keys='Income.saved_account_id')


class Budget(Base):
  __tablename__ = "budget"
  id = Column(Integer, primary_key=True)
  name = Column(String)
  amount = Column(Numeric(10, 2))
  importance = Column(Enum("essential", "discretionary", "excess", name="budget_importance_enum"))
  category_id = Column(Integer, ForeignKey(BudgetCategories.id))

  account_type = relationship(BudgetCategories)


class Expenses(Base):
  __tablename__ = "expenses"
  id = Column(Integer, primary_key=True)
  amount = Column(Numeric(10, 2))
  expense_date = Column(TIMESTAMP)
  paid_to = Column(String)
  budget_entry_id = Column(Integer, ForeignKey(Budget.id), nullable=True)  # null for other
  account_id = Column(Integer, ForeignKey(Account.id))

  budget_category = relationship(Budget)
  account_type = relationship(Account)
