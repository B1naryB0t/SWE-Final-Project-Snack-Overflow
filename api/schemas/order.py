from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .payment import Payment, PaymentCreate

class OrderCreate(BaseModel):
    date: datetime
    status: str
    order_type: str
    customer_id: Optional[int] = None
    guest_name: Optional[str] = None
    guest_email: Optional[str] = None
    guest_phone: Optional[str] = None
    promotion_id: Optional[int] = None
    payments: List[PaymentCreate] = []
    menu_item_ids: List[int] = []

    class ConfigDict:
        from_attributes = True

class OrderUpdate(BaseModel):
    date: Optional[datetime] = None
    status: Optional[str] = None
    order_type: Optional[str] = None
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
    order_type: str
    tracking_number: int
    customer_id: Optional[int] = None
    guest_name: Optional[str] = None
    guest_email: Optional[str] = None
    guest_phone: Optional[str] = None
    promotion_id: Optional[int] = None
    payments: List[Payment] = []

    class ConfigDict:
        from_attributes = True