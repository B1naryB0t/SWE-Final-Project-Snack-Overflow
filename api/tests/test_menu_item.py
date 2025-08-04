def test_delete_menu_item_ingredient(client, test_data):
	r = client.delete(f"/menu_item_ingredient/{test_data['mii_ids'][0]}")
	assert r.status_code in (200, 204)
	assert client.get(f"/menu_item_ingredient/{'mii_id'}").status_code in (404, 422)


def test_read_menu_item_by_category(client, test_data):
	r = client.get(f"/menu_item/by_category/Appetizer")
	assert r.status_code == 200
	items = r.json()
	assert any(item["name"] == "Caesar Salad" for item in items)
	r = client.get("/menu_item/by_category/Dessert")
	assert r.status_code == 200
	assert r.json() == []


def test_read_menu_item_by_rating(client, test_data):
	r = client.get(f"/menu_item/by_rating/4")
	assert r.status_code == 200


def test_delete_menu_item(client, test_data):
	r = client.delete(f"/menu_item/{test_data['menu_item_ids'][0]}")
	assert r.status_code in (200, 204)
	assert client.get(f"/menu_item/{'menu_item_id'}").status_code in (404, 422)
