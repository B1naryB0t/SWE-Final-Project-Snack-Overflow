from typing import Optional

from pydantic import BaseModel


class MenuItemBase(BaseModel):
	id: int
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

	class ConfigDict:
		from_attributes = True


class MenuItemUpdate(BaseModel):
	name: Optional[str] = None
	category: Optional[str] = None
	price: Optional[float] = None
	calories: Optional[int] = None

	class ConfigDict:
		from_attributes = True
