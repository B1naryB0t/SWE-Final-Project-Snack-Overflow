from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Order(Base):
	__tablename__ = "order"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	date = Column(DateTime, nullable=False)
	status = Column(String(20), nullable=False)
	total = Column(Float, nullable=False)
	customer_id = Column(Integer, ForeignKey("customer.id"))

	order_item = relationship("OrderItem", back_populates="order")
	payment = relationship("Payment", back_populates="order")
