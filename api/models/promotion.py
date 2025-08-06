from sqlalchemy import Column, Integer, String, DateTime, Float

from ..dependencies.database import Base


class Promotion(Base):
	__tablename__ = "promotion"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	code = Column(String(50), index=True, unique=True)
	discount_amount = Column(Float, nullable=False)
	expiration_date = Column(DateTime, nullable=False)
