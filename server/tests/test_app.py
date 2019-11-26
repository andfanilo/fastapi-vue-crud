from server.src.app import Book

INITIAL_BOOKS = [
    Book(title="On the Road", author="Jack Kerouac", read=True),
    Book(
        title="Harry Potter and the Philosopher's Stone",
        author="J. K. Rowling",
        read=False,
    ),
    Book(title="Green Eggs and Ham", author="Dr. Seuss", read=True),
]


def _convert_data_to_books(arr):
    return [Book(**book) for book in arr]


def test_index(test_client):
    response = test_client.get("")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["code"] == 200
    assert data["data"] == "Welcome, please check /docs or /redoc"


def test_ping(test_client):
    response = test_client.get("/ping")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["code"] == 200
    assert data["messages"] == []
    assert data["data"] == "Pong!"


def test_get_all_books(test_client):
    response = test_client.get("/books")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["code"] == 200
    assert data["messages"] == []

    books = _convert_data_to_books(data["data"])
    assert books == INITIAL_BOOKS


def test_create_book(test_client):
    create_book = Book(title="Hello", author="World", read=True)
    response = test_client.post("/books", json=create_book.dict())
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["code"] == 200
    assert data["messages"] == ["Book added !"]
    assert data["data"] == create_book

    books = _convert_data_to_books(test_client.get("/books").json()["data"])
    assert books == INITIAL_BOOKS + [create_book]
