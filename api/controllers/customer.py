from sqlalchemy.orm import Session
from fastapi import status, Response
from ..models import customer as model


def create(db: Session, customer):
    db_recipe = model.Customer(
        name=customer.name,
        email=customer.email,
        phone=customer.phone
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def read_all(db: Session):
    return db.query(model.Customer).all()


def read_one(db: Session, customer_id):
    return db.query(model.Customer).filter(model.Customer.id == customer_id).first()


def update(db: Session, customer_id, customer):
    db_customer = db.query(model.Customer).filter(model.Customer.id == customer_id)
    update_data = customer.model_dump(exclude_unset=True)
    db_customer.update(update_data, synchronize_session=False)
    db.commit()
    return db_customer.first()


def delete(db: Session, customer_id):
    db_customer = db.query(model.Customer).filter(model.Customer.id == customer_id)
    db_customer.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
