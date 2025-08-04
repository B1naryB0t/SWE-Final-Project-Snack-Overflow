def test_delete_ingredient(client, test_data):
	r = client.delete(f"/ingredient/{test_data['ingredient_id']}")
	assert r.status_code in (200, 204)
	assert client.get(f"/ingredient/{test_data['ingredient_id']}").status_code in (404, 422)


def test_track_ingredient_inventory(client, test_data):
	response = client.get("/ingredient/")
	assert response.status_code == 200

	ingredients = response.json()
	assert isinstance(ingredients, list)
	assert len(ingredients) > 0

	ingredient = next((ing for ing in ingredients if ing["id"] == test_data["ingredient_id"]), None)
	assert ingredient is not None, "Ingredient not found in list"

	assert "quantity" in ingredient
	assert isinstance(ingredient["quantity"], (int, float))
	assert ingredient["quantity"] >= 0


def test_ingredient_stock_validation(client, test_data):
	ingredient_id = test_data["ingredient_id"]

	r = client.get(f"/ingredient/{ingredient_id}")
	assert r.status_code == 200
	ingredient = r.json()
	available_quantity = ingredient["quantity"]

	excessive_quantity_payload = {
		"menu_item_id": test_data["menu_item_id"],
		"ingredient_id": ingredient_id,
		"quantity": available_quantity + 1000
	}
	r = client.post("/menu_item_ingredient/", json=excessive_quantity_payload)
	assert r.status_code in (400, 422)

	valid_quantity_payload = {
		"menu_item_id": test_data["menu_item_id"],
		"ingredient_id": ingredient_id,
		"quantity": available_quantity - 1 if available_quantity > 1 else available_quantity
	}
	r = client.post("/menu_item_ingredient/", json=valid_quantity_payload)
	assert r.status_code in (200, 201)
