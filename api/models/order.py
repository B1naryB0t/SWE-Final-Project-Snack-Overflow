from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "order"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	date = Column(DateTime, nullable=False)
	status = Column(String(20), nullable=False)
	total = Column(Float, nullable=False)
	order_type = Column(String(20), nullable=False)
	tracking_number = Column(Integer, nullable=True, unique=True)
	customer_id = Column(Integer, ForeignKey("customer.id"), nullable=True)

	customer = relationship("Customer", back_populates="orders")
	order_items = relationship("OrderItem", back_populates="order")
	payments = relationship("Payment", back_populates="order")
