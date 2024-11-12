from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders/", json={
        "customer_name": "John Doe",
        "total_amount": 100,
        "currency": "EUR"
    })
    assert response.status_code == 200
    assert response.json()["customer_name"] == "John Doe"

def test_update_order_status():
    client.post("/orders/", json={"customer_name": "Jane Doe", "total_amount": 150, "currency": "USD"})
    response = client.put("/orders/1", json={"status": "shipped"})
    assert response.status_code == 200
    assert response.json()["status"] == "shipped"
