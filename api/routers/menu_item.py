from fastapi import APIRouter, Depends, Query
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
	"""Create a new menu item."""
	return controller.create(db=db, menu_item=request)


@router.get("/", response_model=list[schema.MenuItem])
def read_all(db: Session = Depends(get_db)):
	"""Get all menu items."""
	return controller.read_all(db)


@router.get("/by_tag", response_model=list[schema.MenuItem])
def read_by_tag(tag: str, db: Session = Depends(get_db)):
	"""Get menu items filtered by tag."""
	return controller.read_by_tag(db, tag=tag)


@router.get("/search", response_model=list[schema.MenuItem])
def search_menu_items(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
	"""Search for menu items by name."""
	return controller.search_menu_items(db, q)


@router.get("/popularity_insights")
def popularity_insights(db: Session = Depends(get_db)):
	"""Get popularity insights for menu items."""
	return controller.get_popularity_insights(db)


@router.get("/by_category/{category}", response_model=list[schema.MenuItem])
def read_by_category(category: str, db: Session = Depends(get_db)):
	"""Get menu items by category."""
	return controller.read_by_category(db, category=category)


@router.get("/by_rating/{rating}", response_model=list[schema.MenuItem])
def read_by_rating(rating: int, db: Session = Depends(get_db)):
	"""Get menu items by rating."""
	return controller.read_by_rating(db, rating=rating)


@router.get("/{menu_item_id}", response_model=schema.MenuItem)
def read_one(menu_item_id: int, db: Session = Depends(get_db)):
	"""Get a menu item by ID."""
	return controller.read_one(db, menu_item_id=menu_item_id)


@router.put("/{menu_item_id}", response_model=schema.MenuItem)
def update(menu_item_id: int, request: schema.MenuItemUpdate, db: Session = Depends(get_db)):
	"""Update a menu item by ID."""
	return controller.update(db=db, menu_item=request, menu_item_id=menu_item_id)


@router.delete("/{menu_item_id}", status_code=204)
def delete_menu_item(menu_item_id: int, db: Session = Depends(get_db)):
	"""Delete a menu item by ID."""
	return controller.delete(db, menu_item_id=menu_item_id)
