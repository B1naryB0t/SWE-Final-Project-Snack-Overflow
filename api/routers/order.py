from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import order as controller
from ..dependencies.database import get_db
from ..schemas import order as schema

router = APIRouter(
	tags=['Orders'],
	prefix="/order"
)


@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
	return controller.create(db=db, order=request)


@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
	return controller.read_all(db)


@router.get("/{order_id}", response_model=schema.Order)
def read_one(order_id: int, db: Session = Depends(get_db)):
	return controller.read_one(db, order_id=order_id)


@router.get("/", response_model=list[schema.Order])
def read_by_date_range(start_date: str, end_date: str, db: Session = Depends(get_db)):
	return controller.read_by_date_range(db, start_date=start_date, end_date=end_date)


@router.get("/track/{tracking_number}", response_model=schema.Order)
def read_by_tracking_number(tracking_number: int, db: Session = Depends(get_db)):
	return controller.read_by_tracking_number(db, tracking_number=tracking_number)


@router.put("/{order_id}", response_model=schema.Order)
def update(order_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
	return controller.update(db=db, order=request, order_id=order_id)


@router.delete("/{order_id}")
def delete(order_id: int, db: Session = Depends(get_db)):
	return controller.delete(db=db, order_id=order_id)
