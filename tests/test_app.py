from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthz():
    assert client.get("/healthz").status_code == 200


def test_readyz():
    assert client.get("/readyz").status_code == 200
