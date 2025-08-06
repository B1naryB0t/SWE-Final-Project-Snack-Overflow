from pydantic import BaseModel


class TopCustomer(BaseModel):
	name: str
	email: str
	total_spent: float
