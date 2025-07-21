from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import promotion as controller
from ..dependencies.database import get_db
from ..schemas import promotion as schema

router = APIRouter(
    tags=['Promotions'],
    prefix="/promotion"
)


@router.post("/", response_model=schema.PromotionBase)
def create(request: schema.PromotionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, promotion=request)


@router.get("/", response_model=list[schema.PromotionBase])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{promotion_id}", response_model=schema.PromotionBase)
def read_one(promotion_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, promotion_id=promotion_id)


@router.put("/{promotion_id}", response_model=schema.PromotionBase)
def update(promotion_id: int, request: schema.PromotionUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, promotion=request, promotion_id=promotion_id)


@router.delete("/{promotion_id}")
def delete(promotion_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, promotion_id=promotion_id)
