from fastapi import status, Response
from sqlalchemy.orm import Session

from ..models import menu_item as model


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