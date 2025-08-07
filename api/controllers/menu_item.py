from fastapi import status, Response
from sqlalchemy import or_, func
from sqlalchemy.orm import Session

from ..models import menu_item as model
from ..models import order_item, review
from ..models import review as model_review


def create(db: Session, menu_item):
	db_menu_item = model.MenuItem(
		name=menu_item.name,
		category=menu_item.category,
		price=menu_item.price,
		calories=menu_item.calories
	)
	db.add(db_menu_item)
	db.commit()
	db.refresh(db_menu_item)
	return db_menu_item


def read_all(db: Session):
	return db.query(model.MenuItem).all()


def read_one(db: Session, menu_item_id):
	return db.query(model.MenuItem).filter(model.MenuItem.id == menu_item_id).first()


def read_by_category(db: Session, category: str):
	return db.query(model.MenuItem).filter(model.MenuItem.category == category).all()


def read_by_rating(db: Session, rating: int):
	return db.query(model.MenuItem).join(model_review.Review).filter(model_review.Review.rating == rating).all()

def read_by_tag(db, tag: str):
    from ..models.menu_item import MenuItem
    return db.query(MenuItem).filter(MenuItem.tags.ilike(f"%{tag}%")).all()

def update(db: Session, menu_item_id, menu_item):
	db_menu_item = db.query(model.MenuItem).filter(model.MenuItem.id == menu_item_id)
	update_data = menu_item.model_dump(exclude_unset=True)
	db_menu_item.update(update_data, synchronize_session=False)
	db.commit()
	return db_menu_item.first()


def delete(db: Session, menu_item_id):
	db_menu_item = db.query(model.MenuItem).filter(model.MenuItem.id == menu_item_id)
	db_menu_item.delete(synchronize_session=False)
	db.commit()
	return Response(status_code=status.HTTP_204_NO_CONTENT)


def search_menu_items(db, query):
	return db.query(model.MenuItem).filter(
		or_(
			model.MenuItem.name.ilike(f"%{query}%"),
		)
	).all()


def get_popularity_insights(db, min_rating=3):
	order_counts = (
		db.query(
			model.MenuItem.id,
			model.MenuItem.name,
			func.count(order_item.OrderItem.id).label("order_count")
		)
		.outerjoin(order_item.OrderItem, model.MenuItem.id == order_item.OrderItem.menu_item_id)
		.group_by(model.MenuItem.id)
		.all()
	)

	complaint_counts = (
		db.query(
			review.Review.menu_item_id,
			func.count(review.Review.id).label("complaint_count")
		)
		.filter(review.Review.rating <= min_rating)
		.group_by(review.Review.menu_item_id)
		.all()
	)

	complaint_dict = {c.menu_item_id: c.complaint_count for c in complaint_counts}

	insights = []
	for item in order_counts:
		insights.append({
			"menu_item_id": item.id,
			"name": item.name,
			"order_count": item.order_count,
			"complaint_count": complaint_dict.get(item.id, 0)
		})
	return insights
