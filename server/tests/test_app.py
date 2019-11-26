from starlette.testclient import TestClient

from server.src.app import app, Book, BOOKS

client = TestClient(app)


def test_index():
    response = client.get("")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["code"] == 200
    assert data["data"] == "Welcome, please check /docs or /redoc"


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["code"] == 200
    assert data["messages"] == []
    assert data["data"] == "Pong!"


def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["code"] == 200
    assert data["messages"] == []

    books = data["data"]
    assert [Book(**book) for book in books] == BOOKS
