from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Payment(Base):
	__tablename__ = "payment"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	status: str = Column(String(20), nullable=False)
	type: str = Column(String(20), nullable=False)
	transaction_id: str = Column(String(20), nullable=False)
	order_id = Column(Integer, ForeignKey("order.id"))

	order = relationship("Order", back_populates="payments")
