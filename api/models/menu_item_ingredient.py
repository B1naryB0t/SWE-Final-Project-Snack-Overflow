from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from ..dependencies.database import Base

class MenuItemIngredient(Base):
    __tablename__ = "menu_item_ingredient"
    id = Column(Integer, primary_key=True, index=True)
    menu_item_id = Column(Integer, ForeignKey("menu_item.id", ondelete="CASCADE"))
    ingredient_id = Column(Integer, ForeignKey("ingredient.id", ondelete="CASCADE"))
    quantity = Column(Float, nullable=False)  # Quantity needed per menu item

    menu_item = relationship("MenuItem", back_populates="menu_item_ingredients")
    ingredient = relationship("Ingredient", back_populates="menu_item_ingredients")