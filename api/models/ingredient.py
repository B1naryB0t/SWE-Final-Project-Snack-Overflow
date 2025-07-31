from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from ..dependencies.database import Base
from .menu_item_ingredient import MenuItemIngredient
from .menu_item import MenuItem


class Ingredient(Base):
	__tablename__ = "ingredient"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	name = Column(String(50), nullable=False)
	quantity = Column(Float, nullable=False)
	unit = Column(String(50), nullable=False)

	menu_items = relationship("MenuItemIngredient", back_populates="ingredient")
	menu_item_objects = relationship("MenuItem",secondary=MenuItemIngredient.__table__,back_populates="ingredient_objects")