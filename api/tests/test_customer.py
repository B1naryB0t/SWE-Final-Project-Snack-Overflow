import random

import pytest
from fastapi.testclient import TestClient
import uuid
from ..main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def test_data():
	data = {}

	# Create Customer
	customer = {
		"name": "Alice",
		"email": "alice@example.com",
		"phone": "1234567890",
	}
	r = client.post("/customer/", json=customer)
	assert r.status_code in (200, 201)
	data["customer_id"] = r.json()["id"]

	# Create Ingredient
	ingredient = {
		"name": "Lettuce",
		"quantity": 50.0,
		"unit": "grams"
	}
	r = client.post("/ingredient/", json=ingredient)
	assert r.status_code in (200, 201)
	data["ingredient_id"] = r.json()["id"]

	# Create Menu Item
	menu_item = {
		"name": "Caesar Salad",
		"category": "Appetizer",
		"price": 7.50,
		"calories": 250
	}
	r = client.post("/menu_item/", json=menu_item)
	assert r.status_code in (200, 201)
	data["menu_item_id"] = r.json()["id"]

	# Link Ingredient to Menu Item
	mii = {
		"menu_item_id": data["menu_item_id"],
		"ingredient_id": data["ingredient_id"]
	}
	r = client.post("/menu_item_ingredient/", json=mii)
	assert r.status_code in (200, 201)
	data["mii_id"] = r.json()["id"]

	# Create Order
	order = {
		"date": "2025-07-24",
		"status": "pending",
		"total": 15.0,
		"order_type": "takeout",
		"tracking_number": random.randint(0, 9999),
		"customer_id": data["customer_id"]
	}
	r = client.post("/order/", json=order)
	assert r.status_code in (200, 201)
	data["order_id"] = r.json()["id"]
	data["tracking_number"] = r.json()["tracking_number"]

	# Add Menu Item to Order
	order_item = {
		"order_id": data["order_id"],
		"menu_item_id": data["menu_item_id"],
		"quantity": 2
	}
	r = client.post("/order_item/", json=order_item)
	assert r.status_code in (200, 201)
	data["order_item_id"] = r.json()["id"]

	# Add Payment
	payment = {
		"order_id": data["order_id"],
		"status": "paid",
		"type": "credit_card",
		"total": 15.0,
		"transaction_id": "txn_001"
	}
	r = client.post("/payment/", json=payment)
	assert r.status_code in (200, 201)
	data["payment_id"] = r.json()["id"]

	# Add Promotion
	promo = {
		"code": str(uuid.uuid4()), # Random code for uniqueness
		"discount_amount": 25.0,
		"expiration_date": "2025-12-31"
	}
	r = client.post("/promotion/", json=promo)
	assert r.status_code in (200, 201)
	data["promotion_id"] = r.json()["id"]

	# Add Review
	review = {
		"customer_id": data["customer_id"],
		"menu_item_id": data["menu_item_id"],
		"rating": 4,
		"comment": "Great!"
	}
	r = client.post("/review/", json=review)
	assert r.status_code in (200, 201)
	data["review_id"] = r.json()["id"]

	return data



def test_read_customer(test_data):
	r = client.get(f"/customer/{test_data['customer_id']}")
	assert r.status_code == 200
	r_data = r.json()
	assert r_data["name"] == "Alice"
	assert r_data["email"] == "alice@example.com"
	assert r_data["phone"] == "1234567890"


def test_delete_customer(test_data):
	r = client.delete(f"/customer/{test_data['customer_id']}")
	assert r.status_code in (200, 204)
	assert client.get(f"/customer/customer_id").status_code in (404 , 422)
