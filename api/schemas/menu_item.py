from typing import Optional, List

from pydantic import BaseModel

from .ingredient import Ingredient

class MenuItemBase(BaseModel):
	name: str
	category: str
	price: float
	calories: int

	class ConfigDict:
		from_attributes = True


class MenuItemCreate(MenuItemBase):
	name: str
	category: str
	price: float
	calories: int
	ingredient_ids: Optional[List[int]] = None

	class ConfigDict:
		from_attributes = True


class MenuItemUpdate(BaseModel):
	name: Optional[str] = None
	category: Optional[str] = None
	price: Optional[float] = None
	calories: Optional[int] = None

	class ConfigDict:
		from_attributes = True


class MenuItem(MenuItemBase):
	id: int
	ingredients: List[Ingredient] = []

	class ConfigDict:
		from_attributes = True
