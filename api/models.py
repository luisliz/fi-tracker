from sqlalchemy import Boolean, Column, ForeignKey, Numeric, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name= Column(String)
    balance= Column(Numeric(10, 2))
    account_type= Column(String)
    account_name= Column(String)
