from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel

from .payment import Payment, PaymentInOrder


class OrderType(str, Enum):
	dine_in = "dine-in"
	takeout = "takeout"
	delivery = "delivery"


class OrderCreate(BaseModel):
	date: datetime
	status: str
	order_type: OrderType
	customer_id: Optional[int] = None
	guest_name: Optional[str] = None
	guest_email: Optional[str] = None
	guest_phone: Optional[str] = None
	promotion_id: Optional[int] = None
	payments: List[PaymentInOrder] = []
	menu_item_ids: List[int] = []

	class ConfigDict:
		from_attributes = True


class OrderUpdate(BaseModel):
	date: Optional[datetime] = None
	status: Optional[str] = None
	order_type: Optional[OrderType] = None
	customer_id: Optional[int] = None
	guest_name: Optional[str] = None
	guest_email: Optional[str] = None
	guest_phone: Optional[str] = None
	promotion_id: Optional[int] = None

	class ConfigDict:
		from_attributes = True


class Order(BaseModel):
	id: int
	date: datetime
	status: str
	total: float
	order_type: OrderType
	tracking_number: int
	customer_id: Optional[int] = None
	guest_name: Optional[str] = None
	guest_email: Optional[str] = None
	guest_phone: Optional[str] = None
	promotion_id: Optional[int] = None
	payments: List[Payment] = []

	class ConfigDict:
		from_attributes = True
