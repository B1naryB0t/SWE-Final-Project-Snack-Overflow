from fastapi import status, Response
from sqlalchemy.orm import Session

from ..models import payment as model


def create(db: Session, payment):
	db_payment = model.Payment(
		status=payment.status,
		type=payment.type,
		transaction_id=payment.transaction_id,
		order_id=payment.order_id
	)
	db.add(db_payment)
	db.commit()
	db.refresh(db_payment)
	return db_payment


def read_all(db: Session):
	return db.query(model.Payment).all()


def read_one(db: Session, payment_id):
	return db.query(model.Payment).filter(model.Payment.id == payment_id).first()


def update(db: Session, payment_id, payment):
	db_payment = db.query(model.Payment).filter(model.Payment.id == payment_id)
	update_data = payment.model_dump(exclude_unset=True)
	db_payment.update(update_data, synchronize_session=False)
	db.commit()
	return db_payment.first()


def delete(db: Session, payment_id):
	db_payment = db.query(model.Payment).filter(model.Payment.id == payment_id)
	db_payment.delete(synchronize_session=False)
	db.commit()
	return Response(status_code=status.HTTP_204_NO_CONTENT)
