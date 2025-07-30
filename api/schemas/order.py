from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OrderBase(BaseModel):
	date: datetime
	status: str
	total: float
	order_type: str
	tracking_number: int
	customer_id: int

	class ConfigDict:
		from_attributes = True


class OrderCreate(OrderBase):
	date: datetime
	status: str
	total: float
	order_type: str
	tracking_number: int
	customer_id: int

	class ConfigDict:
		from_attributes = True


class OrderUpdate(BaseModel):
	date: Optional[datetime] = None
	status: Optional[str] = None
	total: Optional[float] = None
	order_type: Optional[str] = None
	tracking_number: Optional[int] = None
	customer_id: Optional[int] = None

	class ConfigDict:
		from_attributes = True


class Order(OrderBase):
	id: int

	class ConfigDict:
		from_attributes = True
