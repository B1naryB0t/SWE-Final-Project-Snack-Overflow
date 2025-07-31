from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from ..dependencies.database import Base
from .ingredient import Ingredient
from .menu_item_ingredient import MenuItemIngredient


class MenuItem(Base):
	__tablename__ = "menu_item"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	name = Column(String(50), nullable=False)
	category = Column(String(20), nullable=False)
	price = Column(Float, nullable=False)
	calories = Column(Integer, nullable=False)


	order_items = relationship("OrderItem", back_populates="menu_item")
	ingredients = relationship("MenuItemIngredient", back_populates="menu_item")
	ingredient_objects = relationship("Ingredient",secondary=MenuItemIngredient.__table__,back_populates="menu_item_objects")
	reviews = relationship("Review", back_populates="menu_item")
