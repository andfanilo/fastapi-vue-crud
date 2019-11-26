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


BOOKS = [
    Book(title="On the Road", author="Jack Kerouac", read=True),
    Book(
        title="Harry Potter and the Philosopher's Stone",
        author="J. K. Rowling",
        read=False,
    ),
    Book(title="Green Eggs and Ham", author="Dr. Seuss", read=True),
]


#: Describe all Pydantic Response classes
class ResponseBase(BaseModel):
    status: str
    code: int
    messages: List[str] = []


class PongResponse(ResponseBase):
    data: str


class BooksResponse(ResponseBase):
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
    return {"status": "ok", "code": 200, "data": "Pong!"}


@app.get("/books", response_model=BooksResponse)
def get_all_books():
    return {"status": "ok", "code": 200, "data": BOOKS}


#: Start application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
