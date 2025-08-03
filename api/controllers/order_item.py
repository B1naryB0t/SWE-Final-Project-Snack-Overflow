from fastapi import status, Response
from sqlalchemy.orm import Session

from ..models import order_item as model
from fastapi import HTTPException
from ..models import menu_item_ingredient as mii_model
from ..models import ingredient as ingredient_model
from ..models import menu_item as menu_model


def create(db: Session, order_item):
    menu_item = db.query(menu_model.MenuItem).filter(menu_model.MenuItem.id == order_item.menu_item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    for mii in menu_item.menu_item_ingredients:  # FIXED HERE
        required_qty = mii.quantity * order_item.quantity  # Use mii.quantity (not quantity_required)
        available_qty = mii.ingredient.quantity

        if available_qty < required_qty:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient ingredient: {mii.ingredient.name} (required: {required_qty}, available: {available_qty})"
            )

    # All ingredients are available – deduct and commit
    for mii in menu_item.menu_item_ingredients:  # FIXED HERE
        required_qty = mii.quantity * order_item.quantity
        mii.ingredient.quantity -= required_qty

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