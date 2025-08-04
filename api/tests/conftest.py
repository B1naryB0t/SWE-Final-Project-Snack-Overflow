import random
import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import MetaData

from api.dependencies.database import engine
from ..main import app


@pytest.fixture(scope="function", autouse=True)
def clean_db():
	meta = MetaData()
	meta.reflect(bind=engine)
	with engine.connect() as conn:
		for table in reversed(meta.sorted_tables):
			conn.execute(table.delete())
	yield


@pytest.fixture(scope="module")
def client():
	return TestClient(app)


@pytest.fixture(scope="function")
def test_data(client):
	data = {
		"customer_ids": [],
		"ingredient_ids": [],
		"menu_item_ids": [],
		"mii_ids": [],
		"order_ids": [],
		"order_item_ids": [],
		"payment_ids": [],
		"promotion_ids": [],
		"review_ids": []
	}

	# Create Customers
	customers = [
		{"name": "Alice", "email": "alice@example.com", "phone": "1234567890"},
		{"name": "Bob", "email": "bob@example.com", "phone": "2345678901"},
		{"name": "Charlie", "email": "charlie@example.com", "phone": "3456789012"},
	]
	for customer in customers:
		r = client.post("/customer/", json=customer)
		assert r.status_code in (200, 201)
		data["customer_ids"].append(r.json()["id"])

	# Create Ingredients
	ingredients = [
		{"name": "Lettuce", "quantity": 100.0, "unit": "grams"},
		{"name": "Tomato", "quantity": 100.0, "unit": "grams"},
		{"name": "Cheese", "quantity": 100.0, "unit": "grams"},
		{"name": "Bread", "quantity": 100.0, "unit": "pieces"},
		{"name": "Chicken", "quantity": 200.0, "unit": "grams"},
		{"name": "Bacon", "quantity": 100.0, "unit": "grams"},
	]
	for ingredient in ingredients:
		r = client.post("/ingredient/", json=ingredient)
		assert r.status_code in (200, 201)
		data["ingredient_ids"].append(r.json()["id"])

	# Create Menu Items
	menu_items = [
		{"name": "Caesar Salad", "category": "Appetizer", "price": 7.50, "calories": 250},
		{"name": "Chicken Sandwich", "category": "Main", "price": 9.99, "calories": 600},
		{"name": "BLT", "category": "Main", "price": 8.50, "calories": 500},
		{"name": "Grilled Cheese", "category": "Snack", "price": 5.00, "calories": 400},
	]
	for menu_item in menu_items:
		r = client.post("/menu_item/", json=menu_item)
		assert r.status_code in (200, 201)
		data["menu_item_ids"].append(r.json()["id"])

	# Link Ingredients to Each Menu Item
	combinations = [
		[0, 2],         # Caesar Salad -> Lettuce, Cheese
		[4, 3],         # Chicken Sandwich -> Chicken, Bread
		[5, 1, 3],      # BLT -> Bacon, Tomato, Bread
		[2, 3],         # Grilled Cheese -> Cheese, Bread
	]
	for i, ing_indexes in enumerate(combinations):
		for ing_index in ing_indexes:
			mii = {
				"menu_item_id": data["menu_item_ids"][i],
				"ingredient_id": data["ingredient_ids"][ing_index],
				"quantity": 10.0
			}
			r = client.post("/menu_item_ingredient/", json=mii)
			assert r.status_code in (200, 201)
			data["mii_ids"].append(r.json()["id"])

	# Create Order
	order = {
		"date": "2025-07-24",
		"status": "pending",
		"total": 15.0,
		"order_type": "takeout",
		"tracking_number": random.randint(0, 9999999),
		"customer_id": data["customer_ids"][0],
		"menu_item_ids": [data["menu_item_ids"][0]]
	}
	r = client.post("/order/", json=order)
	assert r.status_code in (200, 201)
	data["order_ids"].append(r.json()["id"])
	data["tracking_number"] = r.json()["tracking_number"]

	# Add Menu Item to Order
	order_item = {
		"order_id": data["order_ids"][0],
		"menu_item_id": data["menu_item_ids"][0],
		"quantity": 2
	}
	r = client.post("/order_item/", json=order_item)
	assert r.status_code in (200, 201, 400)
	if r.status_code in (200, 201):
		data["order_item_ids"].append(r.json()["id"])

	# Add Payment
	payment = {
		"order_id": data["order_ids"][0],
		"status": "paid",
		"type": "credit_card",
		"total": 15.0,
		"transaction_id": "txn_001"
	}
	r = client.post("/payment/", json=payment)
	assert r.status_code in (200, 201)
	data["payment_ids"].append(r.json()["id"])

	# Add Promotion
	promo = {
		"code": str(uuid.uuid4()),
		"discount_amount": 25.0,
		"expiration_date": "2025-12-31"
	}
	r = client.post("/promotion/", json=promo)
	assert r.status_code in (200, 201)
	data["promotion_ids"].append(r.json()["id"])

	# Add Review
	review = {
		"customer_id": data["customer_ids"][0],
		"menu_item_id": data["menu_item_ids"][0],
		"rating": 4,
		"comment": "Great!"
	}
	r = client.post("/review/", json=review)
	assert r.status_code in (200, 201)
	data["review_ids"].append(r.json()["id"])

	return data
