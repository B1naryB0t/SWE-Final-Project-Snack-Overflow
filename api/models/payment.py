from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    transaction_id = Column(String(20), nullable=True)
    total = Column(Float, nullable=False)
    order_id = Column(Integer, ForeignKey("order.id", ondelete="CASCADE"))

    order = relationship("Order", back_populates="payments")