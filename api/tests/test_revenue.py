def test_get_revenue(client, test_data):
	r = client.get("/payment/revenue/?start_date=2025-01-01&end_date=2025-12-31")
	assert r.status_code == 200
	assert "total_revenue" in r.json()
	assert "total_orders" in r.json()
	assert "total_customers" in r.json()
	assert r.json()["total_customers"] in range(0, 9999)
