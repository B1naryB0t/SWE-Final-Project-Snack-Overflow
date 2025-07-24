from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(50))
    phone = Column(String(10), index=True, nullable=False)

    orders = relationship("Order", back_populates="customer")
    reviews = relationship("Review", back_populates="customer")
