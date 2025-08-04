import random


def test_read_order_date_range(client, test_data):
	r = client.get("/order?start_date=2025-01-01&end_date=2025-12-31")
	assert r.status_code == 200


def test_read_order_by_tracking(client, test_data):
	r = client.get(f"/order/track/{test_data['tracking_number']}")
	assert r.status_code == 200
	assert isinstance(r.json()["tracking_number"], int)


def test_delete_order_item(client, test_data):
	r = client.delete(f"/order_item/{test_data['order_item_id']}")
	assert r.status_code in (200, 204)
	assert client.get(f"/order_item/{'order_item_id'}").status_code in (404, 422)


def test_delete_order(client, test_data):
	r = client.delete(f"/order/{test_data['order_id']}")
	assert r.status_code in (200, 204)
	assert client.get(f"/order/{'order_id'}").status_code in (404, 422)


def test_place_order(client, test_data):
	order_payload = {
		"date": "2025-08-02T00:00:00",
		"status": "pending",
		"total": 12.0,
		"order_type": "takeout",
		"tracking_number": random.randint(0, 9999),
		"customer_id": test_data["customer_id"],
		"menu_item_ids": [test_data["menu_item_id"]]
	}
	r = client.post("/order", json=order_payload)
	assert r.status_code == 200


def test_track_order_status(client, test_data):
	order_id = test_data["order_id"]

	r = client.get(f"/order/{order_id}")
	assert r.status_code == 200

	order = r.json()
	assert "status" in order
	assert isinstance(order["status"], str)
	assert order["status"] in ["pending", "completed", "cancelled", "shipped", "delivered"]

	tracking_number = test_data["tracking_number"]
	r2 = client.get(f"/order/track/{tracking_number}")
	assert r2.status_code == 200

	order2 = r2.json()
	assert "status" in order2
	assert order2["status"] == order["status"]

def test_guest_checkout(client, test_data):
    order_payload = {
        "date": "2025-08-02T00:00:00",
        "status": "pending",
        "total": 15.0,
        "order_type": "takeout",
        "tracking_number": random.randint(10000, 99999),
        "menu_item_ids": [test_data["menu_item_id"]],
        # No customer_id!
        "guest_name": "Guest User",
        "guest_email": "guest@example.com",
        "guest_phone": "555-5555"
    }
    r = client.post("/order", json=order_payload)
    assert r.status_code == 200
    data = r.json()
    assert data["guest_name"] == "Guest User"
    assert data["customer_id"] is None

def test_guest_checkout_with_promotion(client, test_data):
    order_payload = {
        "date": "2025-08-02T00:00:00",
        "status": "pending",
        "total": 20.0,
        "order_type": "takeout",
        "tracking_number": random.randint(10000, 99999),
        "menu_item_ids": [test_data["menu_item_id"]],
        "guest_name": "Promo Guest",
        "guest_email": "promo@example.com",
        "guest_phone": "555-1234",
        "promotion_id": test_data["promotion_id"]
    }
    r = client.post("/order", json=order_payload)
    assert r.status_code == 200
    data = r.json()
    assert data["guest_name"] == "Promo Guest"
    assert data["promotion_id"] == test_data["promotion_id"]