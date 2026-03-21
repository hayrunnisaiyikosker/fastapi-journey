from fastapi import APIRouter, HTTPException
from models import Book
import asyncio

book_router = APIRouter()

#Mock database of book
books = [
    {"book_id":1, "title": "Animal Farm", "author": "George Orwell", "page_count": 112, "borrow_records": []},
    {"book_id":2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "page_count": 336, "borrow_records": []},
    {"book_id":3, "title": "War And Peace", "author": "Leo Tolstoy", "page_count": 1225, "borrow_records": []},
    {"book_id":4, "title": "The Trial", "author": "Franz Kafka", "page_count": 225, "borrow_records": []},
    {"book_id":5, "title": "Les Miserables", "author": "Victor Hugo", "page_count": 1463, "borrow_records": []},
    {"book_id":7, "title": "Frankestein", "author": "Mary Shelley", "page_count": 280, "borrow_records": []}
]


@book_router.get ("/books/")
async def get_books():
    return books

@book_router.get ("/books/{book_id}")
async def get_book(book_id:int):
    await asyncio.sleep(1)

    for book in books:
        if book["book_id"] == book_id:
            return book
    return {"message": "Book not found"}

@book_router.post ("/books/")
async def add_book(book:Book):
    book_id = max(c["book_id"] for c in books) + 1 if books else 1

    new_book = {
        "book_id": book_id,
        "title": book.title,
        "author": book.author,
        "page_count": book.page_count,
        "borrow_records": book.borrow_records
    }
    
    books.append (new_book)
    return {"message": "New book added successfully", "details": new_book}

@book_router.put ("/books/{book_id}")
async def update_book(book_id:int, updated_book:Book):
    for book in books:
        if book["book_id"] == book_id:
            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["page_count"] = updated_book.page_count
            book["borrow_records"] = updated_book.borrow_records
            return {"message": "Book updated successfully", "book": book}
    return {"message": "Book not found"}

@book_router.delete ("/books/{book_id}")
async def delete_book(book_id:int):
    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
        
    return {"message": "Book not found"}
    