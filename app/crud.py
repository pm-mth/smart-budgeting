# app/crud.py

from http.client import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

# Create an expense
def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(
        amount=expense.amount,
        category=expense.category,
        date=expense.date
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

# Get all expenses
def get_expenses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Expense).offset(skip).limit(limit).all()

# Delete an expense
def delete_expense(db: Session, expense_id: int):
    db_expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if db_expense:
        db.delete(db_expense)
        db.commit()
        return db_expense
    else:
        raise HTTPException(status_code=404, detail="Expense not found")