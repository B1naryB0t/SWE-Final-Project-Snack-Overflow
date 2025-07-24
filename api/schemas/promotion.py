from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PromotionBase(BaseModel):
	code: str
	discount_amount: float
	expiration_date: datetime

	class ConfigDict:
		from_attributes = True


class PromotionCreate(PromotionBase):
	code: str
	discount_amount: float
	expiration_date: datetime

	class ConfigDict:
		from_attributes = True


class PromotionUpdate(BaseModel):
	code: Optional[str] = None
	discount_amount: Optional[float] = None
	expiration_date: Optional[datetime] = None

	class ConfigDict:
		from_attributes = True


class Promotion(PromotionBase):
	id: int

	class ConfigDict:
		from_attributes = True
