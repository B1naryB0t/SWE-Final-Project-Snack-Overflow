from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Review(Base):
	__tablename__ = "review"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	rating = Column(Integer, nullable=False)
	comment = Column(Text, nullable=False)
	customer_id = Column(Integer, ForeignKey("customer.id", ondelete="CASCADE"), nullable=False)
	menu_item_id = Column(Integer, ForeignKey("menu_item.id", ondelete="CASCADE"), nullable=False)
	order_id = Column(Integer, ForeignKey("order.id", ondelete="CASCADE"), nullable=True)

	customer = relationship("Customer", back_populates="reviews")
	menu_item = relationship("MenuItem", back_populates="reviews")
	order = relationship("Order", back_populates="reviews")
