from typing import Optional

from pydantic import BaseModel


class OrderItemBase(BaseModel):
	id: int
	quantity: int
	order_id: int
	menu_item_id: int

	class ConfigDict:
		from_attributes = True


class OrderItemCreate(OrderItemBase):
	menu_item_id: int
	quantity: int
	order_id: int

	class ConfigDict:
		from_attributes = True


class OrderItemUpdate(BaseModel):
	quantity: Optional[int] = None
	order_id: Optional[int] = None
	menu_item_id: Optional[int] = None

	class ConfigDict:
		from_attributes = True
