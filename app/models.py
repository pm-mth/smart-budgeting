# app/models.py

from sqlalchemy import Column, Integer, String, Date, Numeric, TIMESTAMP
from .database import Base

class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Numeric, nullable=False)
    category = Column(String, index=True)
    date = Column(Date)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
