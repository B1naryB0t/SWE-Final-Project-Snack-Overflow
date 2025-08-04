def test_delete_payment(client, test_data):
	r = client.delete(f"/payment/{test_data['payment_id']}")
	assert r.status_code in (200, 204)
	assert client.get(f"/payment/{'payment_id'}").status_code in (404, 422)


def test_make_payment(client, test_data):
	payment = {
		"order_id": test_data["order_id"],
		"status": "paid",
		"type": "credit_card",
		"total": 15.0,
		"transaction_id": "txn_002"
	}
	r = client.post("/payment/", json=payment)
	assert r.status_code in (200, 201)


def test_update_payment(client, test_data):
	updated_payment = {
		"status": "refunded"
	}
	r = client.put(f"/payment/{test_data['payment_id']}", json=updated_payment)
	assert r.status_code == 200
