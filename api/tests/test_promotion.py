import uuid


def test_delete_promotion(client, test_data):
	r = client.delete(f"/promotion/{test_data['promotion_ids'][0]}")
	assert r.status_code in (200, 204)
	assert client.get(f"/promotion/{'promotion_id'}").status_code in (404, 422)


def test_create_promotion(client, test_data):
	promo_payload = {
		"code": str(uuid.uuid4()),
		"discount_amount": 50.0,
		"expiration_date": "2025-12-31"
	}

	response = client.post("/promotion/", json=promo_payload)

	assert response.status_code in (200, 201)

	data = response.json()

	assert data["code"] == promo_payload["code"]
	assert data["discount_amount"] == promo_payload["discount_amount"]
	assert data["expiration_date"].startswith("2025-12-31")
	assert "id" in data
