from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import ingredient as controller
from ..dependencies.database import get_db
from ..schemas import ingredient as schema

router = APIRouter(
    tags=['Ingredients'],
    prefix="/ingredient"
)


@router.post("/", response_model=schema.IngredientBase)
def create(request: schema.IngredientCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, ingredient=request)


@router.get("/", response_model=list[schema.IngredientBase])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{ingredient_id}", response_model=schema.IngredientBase)
def read_one(ingredient_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, ingredient_id=ingredient_id)


@router.put("/{ingredient_id}", response_model=schema.IngredientBase)
def update(ingredient_id: int, request: schema.IngredientUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, ingredient=request, ingredient_id=ingredient_id)


@router.delete("/{ingredient_id}")
def delete(ingredient_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, ingredient_id=ingredient_id)
