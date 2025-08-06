from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_top_customers_analytics():
	response = client.get("/analytics/top-customers")
	assert response.status_code == 200
	data = response.json()
	assert isinstance(data, list)
	assert len(data) <= 3
	for customer in data:
		assert "name" in customer
		assert "email" in customer
		assert "total_spent" in customer
		assert isinstance(customer["total_spent"], float)
