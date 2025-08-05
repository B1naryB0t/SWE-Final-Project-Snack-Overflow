def test_update_review(client, test_data):
	payload = {
		"customer_id": test_data["customer_id"],
		"menu_item_id": test_data["menu_item_id"],
		"rating": 5,
		"comment": "Updated review!"
	}
	before = client.get(f"/review/{test_data['review_id']}")
	r = client.put(f"/review/{test_data['review_id']}", json=payload)
	assert r.status_code == 200
	assert r.json()["comment"] != before.json()["comment"]


def test_read_review_by_menu_item(client, test_data):
	r = client.get(f"/review/menu/{test_data['menu_item_id']}")
	assert r.status_code == 200


def test_delete_review(client, test_data):
	r = client.delete(f"/review/{test_data['review_id']}")
	assert r.status_code in (200, 204)
	assert client.get(f"/review/review_id").status_code in (404, 422)


def test_post_review(client, test_data):
	payload = {
		"customer_id": test_data["customer_id"],
		"menu_item_id": test_data["menu_item_id"],
		"rating": 3,
		"comment": "New review test"
	}
	r = client.post("/review/", json=payload)
	assert r.status_code in (200, 201)

	get_r = client.get(f"/review/menu/{test_data['menu_item_id']}")
	assert get_r.status_code == 200
	assert any(review["comment"] == "New review test" for review in get_r.json())


def test_feedback_analysis(client):
    response = client.get("/review/analysis")
    assert response.status_code == 200
    data = response.json()
    assert "average_rating" in data
    assert "total_reviews" in data
    assert "ratings_breakdown" in data
    assert isinstance(data["ratings_breakdown"], dict)