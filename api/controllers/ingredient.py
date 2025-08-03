from fastapi import status, Response, HTTPException
from sqlalchemy.orm import Session

from ..models import ingredient as model


def create(db: Session, ingredient):
	db_ingredient = model.Ingredient(
		name=ingredient.name,
		quantity=ingredient.quantity,
		unit=ingredient.unit
	)
	db.add(db_ingredient)
	db.commit()
	db.refresh(db_ingredient)
	return db_ingredient


def read_all(db: Session):
	return db.query(model.Ingredient).all()



def read_one(db: Session, ingredient_id):
    ingredient = db.query(model.Ingredient).filter(model.Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient


def update(db: Session, ingredient_id, ingredient):
	db_ingredient = db.query(model.Ingredient).filter(model.Ingredient.id == ingredient_id)
	update_data = ingredient.model_dump(exclude_unset=True)
	db_ingredient.update(update_data, synchronize_session=False)
	db.commit()
	return db_ingredient.first()


def delete(db: Session, ingredient_id):
	db_ingredient = db.query(model.Ingredient).filter(model.Ingredient.id == ingredient_id)
	db_ingredient.delete(synchronize_session=False)
	db.commit()
