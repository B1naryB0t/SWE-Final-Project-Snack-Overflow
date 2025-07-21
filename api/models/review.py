from sqlalchemy import Column, Integer, ForeignKey, Text

from ..dependencies.database import Base


class Review(Base):
	__tablename__ = "review"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	rating = Column(Integer, nullable=False)
	comment = Column(Text, nullable=False)
	customer_id = Column(Integer, ForeignKey("customer.id"))
	menu_item_id = Column(Integer, ForeignKey("menu_item.id"))
