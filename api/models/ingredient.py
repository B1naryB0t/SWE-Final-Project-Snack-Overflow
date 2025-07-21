from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Ingredient(Base):
	__tablename__ = "ingredient"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	name = Column(String(50), nullable=False)
	quantity = Column(Float, nullable=False)
	unit = Column(String(50), nullable=False)

	menu_item_ingredient = relationship("MenuItemIngredient", back_populates="ingredient")
