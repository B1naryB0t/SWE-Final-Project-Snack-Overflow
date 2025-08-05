from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..controllers import menu_item_ingredient as controller
from ..dependencies.database import get_db
from ..models.ingredient import Ingredient
from ..schemas import menu_item_ingredient as schema

router = APIRouter(
	tags=['Menu Item Ingredients'],
	prefix="/menu_item_ingredient"
)


@router.post("/", response_model=schema.MenuItemIngredient)
def create(request: schema.MenuItemIngredientCreate, db: Session = Depends(get_db)):
	"""Create a new menu item ingredient."""
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
	"""Get all menu item ingredients."""
	return controller.read_all(db)


@router.get("/{mii_id}", response_model=schema.MenuItemIngredient)
def read_one(mii_id: int, db: Session = Depends(get_db)):
	"""Get a menu item ingredient by ID."""
	return controller.read_one(db, mii_id=mii_id)


@router.put("/{mii_id}", response_model=schema.MenuItemIngredient)
def update(mii_id: int, request: schema.MenuItemIngredientUpdate, db: Session = Depends(get_db)):
	"""Update a menu item ingredient by ID."""
	return controller.update(db=db, menu_item_ingredient=request, mii_id=mii_id)


@router.delete("/{mii_id}")
def delete(mii_id: int, db: Session = Depends(get_db)):
	"""Delete a menu item ingredient by ID."""
	return controller.delete(db=db, mii_id=mii_id)
