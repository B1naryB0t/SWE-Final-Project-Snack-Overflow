from typing import Optional

from pydantic import BaseModel


class PaymentBase(BaseModel):
	status: str
	type: str
	transaction_id: str
	order_id: int

	class ConfigDict:
		from_attributes = True


class PaymentCreate(PaymentBase):
	status: str
	type: str
	transaction_id: str
	order_id: int

	class ConfigDict:
		from_attributes = True


class PaymentUpdate(BaseModel):
	status: Optional[str] = None
	type: Optional[str] = None
	transaction_id: Optional[str] = None
	order_id: Optional[int] = None

	class ConfigDict:
		from_attributes = True


class Payment(PaymentBase):
	id: int

	class ConfigDict:
		from_attributes = True
