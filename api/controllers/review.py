from fastapi import status, Response
from sqlalchemy.orm import Session

from ..models import review as model


def create(db: Session, review):
	db_review = model.Review(
		rating=review.rating,
		comment=review.comment,
		customer_id=review.customer_id,
		menu_item_id=review.menu_item_id
	)
	db.add(db_review)
	db.commit()
	db.refresh(db_review)
	return db_review


def read_all(db: Session):
	return db.query(model.Review).all()


def read_one(db: Session, review_id):
	return db.query(model.Review).filter(model.Review.id == review_id).first()


def read_by_menu_item(db: Session, menu_item_id):
	return db.query(model.Review).filter(model.Review.menu_item_id == menu_item_id).all()


def update(db: Session, review_id, review):
	db_review = db.query(model.Review).filter(model.Review.id == review_id)
	update_data = review.model_dump(exclude_unset=True)
	db_review.update(update_data, synchronize_session=False)
	db.commit()
	return db_review.first()


def delete(db: Session, review_id):
	db_review = db.query(model.Review).filter(model.Review.id == review_id)
	db_review.delete(synchronize_session=False)
	db.commit()
	return Response(status_code=status.HTTP_204_NO_CONTENT)
