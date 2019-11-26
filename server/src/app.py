from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

#: Configure CORS
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#: Initialize list of books
class Book(BaseModel):
    title: str
    author: str
    read: bool


BOOKS: List[Book] = []


@app.on_event("startup")
async def startup_event():
    BOOKS.clear()
    BOOKS.append(Book(title="On the Road", author="Jack Kerouac", read=True))
    BOOKS.append(
        Book(
            title="Harry Potter and the Philosopher's Stone",
            author="J. K. Rowling",
            read=False,
        )
    )
    BOOKS.append(Book(title="Green Eggs and Ham", author="Dr. Seuss", read=True))


#: Describe all Pydantic Response classes
class ResponseBase(BaseModel):
    status: str
    code: int
    messages: List[str] = []


class PongResponse(ResponseBase):
    data: str = "Pong!"


class BookResponse(ResponseBase):
    data: Book


class ListBooksResponse(ResponseBase):
    data: List[Book]


#: Mount routes
@app.get("/")
def index():
    return {
        "status": "ok",
        "code": 200,
        "data": "Welcome, please check /docs or /redoc",
    }


@app.get("/ping", response_model=PongResponse)
def return_pong():
    return {"status": "ok", "code": 200}


@app.get("/books", response_model=ListBooksResponse)
def get_all_books():
    return {"status": "ok", "code": 200, "data": BOOKS}


@app.post("/books", response_model=BookResponse)
def create_book(book: Book):
    BOOKS.append(book)
    return {
        "status": "success",
        "code": 200,
        "messages": ["Book added !"],
        "data": book,
    }


#: Start application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
