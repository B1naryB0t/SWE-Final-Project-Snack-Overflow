from fastapi import status, Response
from sqlalchemy.orm import Session

from ..models import menu_item_ingredient as model


def create(db: Session, menu_item_ingredient):
	db_mii = model.MenuItemIngredient(
		menu_item_id=menu_item_ingredient.menu_item_id,
		ingredient_id=menu_item_ingredient.ingredient_id
	)
	db.add(db_mii)
	db.commit()
	db.refresh(db_mii)
	return db_mii


def read_all(db: Session):
	return db.query(model.MenuItemIngredient).all()


def read_one(db: Session, mii_id):
	return db.query(model.MenuItemIngredient).filter(model.MenuItemIngredient.id == mii_id).first()


def update(db: Session, mii_id, menu_item_ingredient):
	db_mii = db.query(model.MenuItemIngredient).filter(model.MenuItemIngredient.id == mii_id)
	update_data = menu_item_ingredient.model_dump(exclude_unset=True)
	db_mii.update(update_data, synchronize_session=False)
	db.commit()
	return db_mii.first()


def delete(db: Session, mii_id):
	db_mii = db.query(model.MenuItemIngredient).filter(model.MenuItemIngredient.id == mii_id)
	db_mii.delete(synchronize_session=False)
	db.commit()
	return Response(status_code=status.HTTP_204_NO_CONTENT)
