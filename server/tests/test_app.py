from starlette.testclient import TestClient

from server.src.app import app

client = TestClient(app)


def test_index():
    response = client.get("")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    data = response.json()
    assert data["code"] == 200
    assert data["messages"] == []
    assert data["result"] == "Pong!"
    assert data["status"] == "ok"
