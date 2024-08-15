from fastapi.testclient import TestClient
from Homework_13_2.main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/your-route")
    assert response.status_code == 200
    assert response.json() == expected_data
