from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import order_item as controller
from ..dependencies.database import get_db
from ..schemas import order_item as schema

router = APIRouter(
    tags=['Order Items'],
    prefix="/order_item"
)


@router.post("/", response_model=schema.OrderItemBase)
def create(request: schema.OrderItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, order_item=request)


@router.get("/", response_model=list[schema.OrderItemBase])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{order_item_id}", response_model=schema.OrderItemBase)
def read_one(order_item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_item_id=order_item_id)


@router.put("/{order_item_id}", response_model=schema.OrderItemBase)
def update(order_item_id: int, request: schema.OrderItemUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, order_item=request, order_item_id=order_item_id)


@router.delete("/{order_item_id}")
def delete(order_item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, order_item_id=order_item_id)
