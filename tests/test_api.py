from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_fibonacci_endpoint():
    response = client.get("/fibonacci/7")

    assert response.status_code == 200
    assert response.json() == {
        "n": 7,
        "result": 13
    }

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }