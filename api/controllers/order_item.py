from fastapi import status, Response
from sqlalchemy.orm import Session

from ..models import order_item as model


def create(db: Session, order_item):
    db_order_item = model.OrderItem(
        quantity=order_item.quantity,
        order_id=order_item.order_id,
        menu_item_id=order_item.menu_item_id
    )
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item

def read_all(db: Session):
    return db.query(model.OrderItem).all()

def read_one(db: Session, order_item_id):
    return db.query(model.OrderItem).filter(model.OrderItem.id == order_item_id).first()

def update(db: Session, order_item_id, order_item):
    db_order_item = db.query(model.OrderItem).filter(model.OrderItem.id == order_item_id)
    update_data = order_item.model_dump(exclude_unset=True)
    db_order_item.update(update_data, synchronize_session=False)
    db.commit()
    return db_order_item.first()

def delete(db: Session, order_item_id):
    db_order_item = db.query(model.OrderItem).filter(model.OrderItem.id == order_item_id)
    db_order_item.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)