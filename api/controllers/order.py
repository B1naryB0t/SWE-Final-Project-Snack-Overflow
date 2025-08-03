from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from datetime import datetime

from ..models import order as model
from ..models import menu_item, ingredient, order_item, promotion
from ..schemas.order import OrderCreate

def create(db: Session, order: OrderCreate):
    menu_items = db.query(menu_item.MenuItem).filter(menu_item.MenuItem.id.in_(order.menu_item_ids)).all()
    if len(menu_items) != len(order.menu_item_ids):
        raise HTTPException(
            status_code=404,
            detail="One or more menu items not found"
        )

    required_ingredients = {}
    for item in menu_items:
        for mii in item.menu_item_ingredients:  
            ingr = mii.ingredient
            if ingr.id not in required_ingredients:
                required_ingredients[ingr.id] = 0
            required_ingredients[ingr.id] += mii.quantity  # Use the correct quantity

    for ingr_id, required_qty in required_ingredients.items():
        ingr = db.query(ingredient.Ingredient).get(ingr_id)
        if ingr.quantity < required_qty:
            raise HTTPException(
                status_code=400,
                detail=f"Not enough '{ingr.name}' in stock."
            )

    for ingr_id, required_qty in required_ingredients.items():
        ingr = db.query(ingredient.Ingredient).get(ingr_id)
        ingr.quantity -= required_qty

    total_price = sum(item.price for item in menu_items)

    promo_obj = None
    if order.promotion_code:
        promo_obj = db.query(promotion.Promotion).filter(
            promotion.Promotion.code == order.promotion_code,
            promotion.Promotion.expiration_date >= datetime.utcnow()
        ).first()

        if not promo_obj:
            raise HTTPException(
                status_code=400,
                detail="Invalid or expired promotion code"
            )
        total_price -= promo_obj.discount_amount
        total_price = max(total_price, 0)

    db_order = model.Order(
        date=order.date,
        status=order.status,
        total=total_price,
        order_type=order.order_type,
        tracking_number=order.tracking_number,
        customer_id=order.customer_id,
        promotion=promo_obj
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in menu_items:
        db_order_item = order_item.OrderItem(
            order_id=db_order.id,
            menu_item_id=item.id,
            quantity=1
        )
        db.add(db_order_item)

    db.commit()
    return db_order


def read_all(db: Session):
    return db.query(model.Order).all()


def read_one(db: Session, order_id: int):
    order = db.query(model.Order).filter(model.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


def read_by_date_range(db: Session, start_date, end_date):
    return db.query(model.Order).filter(model.Order.date.between(start_date, end_date)).all()


def read_by_tracking_number(db: Session, tracking_number: int):
    order = db.query(model.Order).filter(model.Order.tracking_number == tracking_number).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


def update(db: Session, order_id: int, order):
    db_order = db.query(model.Order).filter(model.Order.id == order_id)
    if not db_order.first():
        raise HTTPException(status_code=404, detail="Order not found")
    update_data = order.model_dump(exclude_unset=True)
    db_order.update(update_data, synchronize_session=False)
    db.commit()
    return db_order.first()


def delete(db: Session, order_id):
    db_order = db.query(model.Order).filter(model.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)