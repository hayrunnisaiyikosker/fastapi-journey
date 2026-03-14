from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

#BorrowRecord Model

class BorrowRecord (BaseModel):
    record_id: int
    borrower_name: str = Field(min_length=3)
    borrower_id: int 
    borrow_date: date
    return_date: Optional[date] = None

#Book Model
class Book (BaseModel):
    book_id: int
    title: str = Field(min_length=3)
    author: str
    page_count: int = Field(gt=0)
    borrow_records: list[BorrowRecord] = []