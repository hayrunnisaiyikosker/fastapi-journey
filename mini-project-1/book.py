from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import Book
import asyncio
from database import managed_db

book_router = APIRouter()

templates = Jinja2Templates(directory="templates")

#Mock database of book


@book_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    with managed_db() as db:
        books = db.get_all()
    return templates.TemplateResponse("home.html", {
        "request": request,
        "books": books
    })


@book_router.get("/book/{id}", response_class=HTMLResponse)
async def get_book_page(request: Request, id: int):
    with managed_db() as db:
        book = db.get(id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with ID {id} was not found")
    return templates.TemplateResponse("book.html", {
        "request": request,
        "book": book
    })
    
    
@book_router.get ("/books/")
async def get_books():
    with managed_db() as db:
        return db.get_all()

@book_router.get ("/books/{book_id}")
async def get_book(book_id:int):
    await asyncio.sleep(1)
    with managed_db() as db:
        book = db.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} was not found")
    return book
    

@book_router.post ("/books/")
async def add_book(book:Book):
    with managed_db() as db:
        new_id = db.create(book)
        new_book = db.get(new_id)
    return {"message": "New book added successfully", "details": new_book}


@book_router.put ("/books/{book_id}")
async def update_book(book_id:int, updated_book:Book):
    with managed_db() as db:
        book = db.update(book_id, updated_book)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with ID {book_id} was not found")
    return {"message": "Book updated successfully", "book": book}

@book_router.delete ("/books/{book_id}")
async def delete_book(book_id:int):
    with managed_db() as db:
        book = db.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail=f"Book with ID {book_id} was not found")
        db.delete(book_id)
    return {"message": "Book deleted successfully"}
    