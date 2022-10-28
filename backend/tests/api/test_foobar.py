from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)


def test_foobar():
    response = client.post("/api/v1/foobar/", json={"number": 1})
    assert response.status_code == 200
    assert response.json() == {"result": "1"}
