import datetime
from typing import Optional

from pydantic import BaseModel


class OrderBase(BaseModel):
	id: int
	date: datetime
	status: str
	total: float
	customer_id: int

	class ConfigDict:
		from_attributes = True


class OrderCreate(OrderBase):
	date: datetime
	status: str
	total: float
	customer_id: int

	class ConfigDict:
		from_attributes = True


class OrderUpdate(BaseModel):
	date: Optional[datetime] = None
	status: Optional[str] = None
	total: Optional[float] = None
	customer_id: Optional[int] = None

	class ConfigDict:
		from_attributes = True
