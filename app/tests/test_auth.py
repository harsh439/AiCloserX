from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login():
    response = client.post("/api/v1/auth/login", json={"username": "user", "password": "pass"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_invalid_login():
    response = client.post("/api/v1/auth/login", json={"username": "invalid", "password": "wrongpass"})
    assert response.status_code == 401
