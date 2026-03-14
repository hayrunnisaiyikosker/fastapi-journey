from fastapi import FastAPI
from models import Book
import asyncio

app = FastAPI()

#Mock database of book

books = [
    {"book_id":1, "title": "Animal Farm", "author": "George Orwell", "page_count": 112, "borrow_records": []},
    {"book_id":2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "page_count": 336, "borrow_records": []},
    {"book_id":3, "title": "War And Peace", "author": "Leo Tolstoy", "page_count": 1225, "borrow_records": []},
    {"book_id":4, "title": "The Trial", "author": "Franz Kafka", "page_count": 225, "borrow_records": []},
    {"book_id":5, "title": "Les Miserables", "author": "Victor Hugo", "page_count": 1463, "borrow_records": []},
    {"book_id":7, "title": "Frankestein", "author": "Mary Shelley", "page_count": 280, "borrow_records": []}
]

@app.get ("/books/")
async def get_books():
    return books

@app.get ("/books/{book_id}")
async def get_book(book_id: int):
    await asyncio.sleep(1)

    for book in books:
        if book["book_id"] == book_id:
            return book
    return {"message": "Book not found"}
        