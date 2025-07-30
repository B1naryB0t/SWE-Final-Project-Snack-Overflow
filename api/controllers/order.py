from fastapi import status, Response
from sqlalchemy.orm import Session

from ..models import order as model


def create(db: Session, order):
	db_order = model.Order(
		date=order.date,
		status=order.status,
		total=order.total,
		order_type=order.order_type,
		tracking_number=order.tracking_number,
		customer_id=order.customer_id
	)
	db.add(db_order)
	db.commit()
	db.refresh(db_order)
	return db_order


def read_all(db: Session):
	return db.query(model.Order).all()


def read_one(db: Session, order_id):
	return db.query(model.Order).filter(model.Order.id == order_id).first()


def update(db: Session, order_id, order):
	db_order = db.query(model.Order).filter(model.Order.id == order_id)
	update_data = order.model_dump(exclude_unset=True)
	db_order.update(update_data, synchronize_session=False)
	db.commit()
	return db_order.first()


def delete(db: Session, order_id):
	db_order = db.query(model.Order).filter(model.Order.id == order_id)
	db_order.delete(synchronize_session=False)
	db.commit()
	return Response(status_code=status.HTTP_204_NO_CONTENT)
