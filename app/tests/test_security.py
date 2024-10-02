from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_data_encryption():
    response = client.post("/api/v1/security/encrypt-data", json={"data": {"email": "test@example.com"}, "encryption_method": "AES-256"})
    assert response.status_code == 200
    assert "encrypted_data" in response.json()

def test_gdpr_data_deletion():
    response = client.post("/api/v1/security/gdpr/request-data-deletion", json={"user_id": "user123", "request_type": "data_deletion", "reason": "user_requested"})
    assert response.status_code == 200
    assert response.json()["status"] == "deletion_initiated"
