from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItemIngredient(Base):
	__tablename__ = "menu_item_ingredient"

	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	menu_item_id = Column(Integer, ForeignKey("menu_item.id"))
	ingredient_id = Column(Integer, ForeignKey("ingredient.id"))

	menu_item = relationship("MenuItem", back_populates="menu_item_ingredient")
