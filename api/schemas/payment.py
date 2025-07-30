from typing import Optional

from pydantic import BaseModel


class PaymentBase(BaseModel):
	status: str
	type: str
	transaction_id: str
	total: float
	order_id: int

	class ConfigDict:
		from_attributes = True


class PaymentCreate(PaymentBase):
	status: str
	type: str
	transaction_id: str
	total: float
	order_id: int

	class ConfigDict:
		from_attributes = True


class PaymentUpdate(BaseModel):
	status: Optional[str] = None
	type: Optional[str] = None
	transaction_id: Optional[str] = None
	total: Optional[float] = None
	order_id: Optional[int] = None

	class ConfigDict:
		from_attributes = True


class Payment(PaymentBase):
	id: int

	class ConfigDict:
		from_attributes = True


class Revenue(BaseModel):
	total_revenue: float
	total_orders: int
	total_customers: int

	class Config:
		from_attributes = True
