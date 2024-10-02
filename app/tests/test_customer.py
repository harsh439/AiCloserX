from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_customer():
    response = client.get("/api/v1/customer/1")
    assert response.status_code == 200
    assert "customer_id" in response.json()
