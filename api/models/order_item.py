from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class OrderItem(Base):
	__tablename__ = "order_item"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	quantity = Column(Integer, nullable=False)
	order_id = Column(Integer, ForeignKey("order.id"))
	menu_item_id = Column(Integer, ForeignKey("menu_item.id"))

	order = relationship("Order", back_populates="order_item")
