from fastapi import status, Response
from sqlalchemy.orm import Session

from ..models import promotion as model


def create(db: Session, promotion):
    db_promotion = model.Promotion(
        code=promotion.code,
        discount_amount=promotion.discount_amount,
        expiration_date=promotion.expiration_date
    )
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

def read_all(db: Session):
    return db.query(model.Promotion).all()

def read_one(db: Session, promotion_id):
    return db.query(model.Promotion).filter(model.Promotion.id == promotion_id).first()

def update(db: Session, promotion_id, promotion):
    db_promotion = db.query(model.Promotion).filter(model.Promotion.id == promotion_id)
    update_data = promotion.model_dump(exclude_unset=True)
    db_promotion.update(update_data, synchronize_session=False)
    db.commit()
    return db_promotion.first()

def delete(db: Session, promotion_id):
    db_promotion = db.query(model.Promotion).filter(model.Promotion.id == promotion_id)
    db_promotion.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)