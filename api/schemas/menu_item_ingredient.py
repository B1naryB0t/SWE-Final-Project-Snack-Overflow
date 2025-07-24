from typing import Optional

from pydantic import BaseModel


class MenuItemIngredientBase(BaseModel):
	menu_item_id: int
	ingredient_id: int

	class ConfigDict:
		from_attributes = True


class MenuItemIngredientCreate(MenuItemIngredientBase):
	menu_item_id: int
	ingredient_id: int

	class ConfigDict:
		from_attributes = True


class MenuItemIngredientUpdate(BaseModel):
	menu_item_id: Optional[int] = None
	ingredient_id: Optional[int] = None

	class ConfigDict:
		from_attributes = True


class MenuItemIngredient(MenuItemIngredientBase):
	id: int

	class ConfigDict:
		from_attributes = True
		orm_mode = True
