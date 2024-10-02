from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_recommendations():
    response = client.post("/api/v1/personalization/recommendations", json={"customer_id": "user123"})
    assert response.status_code == 200
    assert "recommendations" in response.json()
