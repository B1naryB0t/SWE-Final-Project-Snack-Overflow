def test_read_customer(client, test_data):
	r = client.get(f"/customer/{test_data['customer_ids'][0]}")
	assert r.status_code == 200
	r_data = r.json()
	assert r_data["name"] == "Alice"
	assert r_data["email"] == "alice@example.com"
	assert r_data["phone"] == "1234567890"


def test_delete_customer(client, test_data):
	r = client.delete(f"/customer/{test_data['customer_ids'][0]}")
	assert r.status_code in (200, 204)
	assert client.get(f"/customer/customer_id").status_code in (404, 422)
