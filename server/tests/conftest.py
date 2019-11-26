import pytest
from starlette.testclient import TestClient

from server.src.app import app


@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client
