# app/schemas.py

from pydantic import BaseModel
from datetime import date
from typing import Optional

# Pydantic model for creating an expense
class ExpenseBase(BaseModel):
    amount: float
    category: str
    date: date

# Pydantic model for creating an expense (without an ID)
class ExpenseCreate(ExpenseBase):
    pass

# Pydantic model for the response (with an ID and timestamp)
class Expense(ExpenseBase):
    id: int
    created_at: str
    
    class Config:
        orm_mode = True
