from typing import Optional

from pydantic import BaseModel


class ReviewBase(BaseModel):
	rating: int
	comment: str
	customer_id: int
	menu_item_id: int
	order_id: Optional[int] = None

	class ConfigDict:
		from_attributes = True


class ReviewCreate(ReviewBase):
	pass


class ReviewUpdate(BaseModel):
	rating: Optional[int] = None
	comment: Optional[str] = None
	customer_id: Optional[int] = None
	menu_item_id: Optional[int] = None
	order_id: Optional[int] = None

	class ConfigDict:
		from_attributes = True


class Review(ReviewBase):
	id: int

	class ConfigDict:
		from_attributes = True
