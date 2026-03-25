# LIBRARY mini-project-1

## (Models) Why did I choose each Pydantic field type?

### Book
- book_id: I assigned as a int because it's unique identifier for each book.
- title: title is str and (min_length=3); to be sure it's not too short.
- author: author is str and this stores the name of the author.
- page_count: its int and gt=0 it means cannot be negative.
- borrow_records: (list[BorrowRecord]) : nested list of borrow records, its tracking which users borrowed the book.

### BorrowRecord
- record_id: it's int that means unique identifier for each borrow record.
- borrower_name: str and (min_length=3); to be sure the length not too short.
- borrower_id: int because id is unique identifier.
- borrow_date: date because this stores the date the book was borrowed.
- return_date: Optional[date] this means none if the book is not yet returned.


## What does each validation rule protect against?

- "title" and "borrower_name" have "min_length=3" to ensure non-empty and meaningful values.
- "page_count" using "gt=0" because the page_count cannot be negative or zero.
- "return_date" is optional, allowing records to be created even if the book has not been returned.

## Which endpoint uses `async` in a meaningful way, and why?

- The "GET /books/{book_id}" endpoint uses "await asyncio.sleep(1)" to simulate a real-world delay in data retrieval.
- This is for showing how works asynchronous endpoints in FastAPI.

## Endpoints
| `GET` | `/books/` | Return all books |
| `GET` | `/books/{book_id}` | Return a single book with nested borrow records |
| `POST` | `/books/` | Adds a new book |
| `PUT` | `/books/{book_id}` | Updates an existing book |
| `DELETE` | `/books/{book_id}` | deletes a book |

## Database 

### What is the '@contextmanager' and why we are using it here instead of a plain function?
`@contextmanager` is a decorator that makes a generator function usable
within a `with` block. In the `managed_db()` function, we expose the database connection
using `yield db`; when the `with` block ends, `db.close()` within the `finally` block runs automatically. If we had used a plain function, we would have had to manually write the `close()` call in every endpoint, and the connection would not close if an exception occurred.

### What does `check_same_thread=False` do, and why is it necessary in FastAPI?
By default, SQLite only allows the connection to be used by the thread that opened it. However, due to its asynchronous nature, FastAPI can process requests in different threads. Without `check_same_thread=False`, FastAPI throws an error when attempting to access the SQLite connection from a different thread. This setting removes that restriction.

### What happens to the data when the server restarts — a comparison with the old SQLite list?
The old mock list (`books = [...]`) was kept in memory. When the server shut down, all changes (books added, deleted, or updated) were lost, and the list was reloaded from scratch each time. With SQLite, data is written to the `sqlite.db` file. Even if the server restarts, the data remains in the file; nothing is lost.