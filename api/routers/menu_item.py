from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import menu_item as controller
from ..dependencies.database import get_db
from ..schemas import menu_item as schema

router = APIRouter(
	tags=['Menu Items'],
	prefix="/menu_item"
)


@router.post("/", response_model=schema.MenuItem)
def create(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
	return controller.create(db=db, menu_item=request)


@router.get("/", response_model=list[schema.MenuItem])
def read_all(db: Session = Depends(get_db)):
	return controller.read_all(db)


@router.get("/{menu_item_id}", response_model=schema.MenuItem)
def read_one(menu_item_id: int, db: Session = Depends(get_db)):
	return controller.read_one(db, menu_item_id=menu_item_id)


@router.get("/by_category/{category}", response_model=list[schema.MenuItem])
def read_by_category(category: str, db: Session = Depends(get_db)):
	return controller.read_by_category(db, category=category)


@router.get("/by_rating/{rating}", response_model=list[schema.MenuItem])
def read_by_rating(rating: int, db: Session = Depends(get_db)):
	return controller.read_by_rating(db, rating=rating)


@router.put("/{menu_item_id}", response_model=schema.MenuItem)
def update(menu_item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
	return controller.update(db=db, menu_item=request, menu_item_id=menu_item_id)


@router.delete("/{menu_item_id}")
def delete(menu_item_id: int, db: Session = Depends(get_db)):
	return controller.delete(db=db, menu_item_id=menu_item_id)
