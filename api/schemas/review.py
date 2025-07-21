from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
	id: int
	rating: int
	comment: str
	customer_id: int
	menu_item_id: int

	class ConfigDict:
		from_attributes = True


class ReviewCreate(ReviewBase):
	rating: int
	comment: str
	customer_id: int
	menu_item_id: int

	class ConfigDict:
		from_attributes = True


class ReviewUpdate(BaseModel):
	rating: Optional[int] = None
	comment: Optional[str] = None
	customer_id: Optional[int] = None
	menu_item_id: Optional[int] = None

	class ConfigDict:
		from_attributes = True
