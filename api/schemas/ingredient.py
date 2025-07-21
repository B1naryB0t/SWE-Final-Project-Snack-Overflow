from typing import Optional
from pydantic import BaseModel


class IngredientBase(BaseModel):
	id: int
	name: str
	quantity: float
	unit: str

	class ConfigDict:
		from_attributes = True


class IngredientCreate(IngredientBase):
	name: str
	quantity: float
	unit: str

	class ConfigDict:
		from_attributes = True


class IngredientUpdate(BaseModel):
	name: Optional[str] = None
	quantity: Optional[float] = None
	unit: Optional[str] = None

	class ConfigDict:
		from_attributes = True
