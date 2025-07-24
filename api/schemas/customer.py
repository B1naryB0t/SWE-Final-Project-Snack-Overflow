from typing import Optional

from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str

    class ConfigDict:
        from_attributes = True


class CustomerCreate(CustomerBase):
    name: str
    email: str
    phone: str


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

    class ConfigDict:
        from_attributes = True


class Customer(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True
