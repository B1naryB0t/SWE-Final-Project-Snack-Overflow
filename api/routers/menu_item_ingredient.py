"""from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..controllers import menu_item_ingredient as controller
from ..dependencies.database import get_db
from ..schemas import menu_item_ingredient as schema

router = APIRouter(
    tags=['Menu Item Ingredients'],
    prefix="/menu_item_ingredient"
)


@router.post("/", response_model=schema.MenuItemIngredient)
def create(request: schema.MenuItemIngredientCreate, db: Session = Depends(get_db)):
    # Optionally, add inventory check logic here in the future
    return controller.create(db=db, menu_item_ingredient=request)
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..controllers import menu_item_ingredient as controller
from ..dependencies.database import get_db
from ..models.ingredient import Ingredient  # import the Ingredient model here
from ..schemas import menu_item_ingredient as schema

router = APIRouter(
	tags=['Menu Item Ingredients'],
	prefix="/menu_item_ingredient"
)


@router.post("/", response_model=schema.MenuItemIngredient)
def create(request: schema.MenuItemIngredientCreate, db: Session = Depends(get_db)):
	ingredient = db.query(Ingredient).filter(Ingredient.id == request.ingredient_id).first()
	if not ingredient:
		raise HTTPException(status_code=404, detail="Ingredient not found")

	if ingredient.quantity < request.quantity:
		raise HTTPException(
			status_code=422,
			detail=f"Not enough stock for ingredient {ingredient.name}. Available: {ingredient.quantity}, required: {request.quantity}"
		)
	return controller.create(db=db, menu_item_ingredient=request)


@router.get("/", response_model=list[schema.MenuItemIngredient])
def read_all(db: Session = Depends(get_db)):
	return controller.read_all(db)


@router.get("/{mii_id}", response_model=schema.MenuItemIngredient)
def read_one(mii_id: int, db: Session = Depends(get_db)):
	return controller.read_one(db, mii_id=mii_id)


@router.put("/{mii_id}", response_model=schema.MenuItemIngredient)
def update(mii_id: int, request: schema.MenuItemIngredientUpdate, db: Session = Depends(get_db)):
	return controller.update(db=db, menu_item_ingredient=request, mii_id=mii_id)


@router.delete("/{mii_id}")
def delete(mii_id: int, db: Session = Depends(get_db)):
	return controller.delete(db=db, mii_id=mii_id)
