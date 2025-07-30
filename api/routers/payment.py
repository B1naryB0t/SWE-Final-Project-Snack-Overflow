from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import payment as controller
from ..dependencies.database import get_db
from ..schemas import payment as schema

router = APIRouter(
	tags=['Payments'],
	prefix="/payment"
)


@router.post("/", response_model=schema.Payment)
def create(request: schema.PaymentCreate, db: Session = Depends(get_db)):
	return controller.create(db=db, payment=request)


@router.get("/", response_model=list[schema.Payment])
def read_all(db: Session = Depends(get_db)):
	return controller.read_all(db)


@router.get("/{payment_id}", response_model=schema.Payment)
def read_one(payment_id: int, db: Session = Depends(get_db)):
	return controller.read_one(db, payment_id=payment_id)


@router.put("/{payment_id}", response_model=schema.Payment)
def update(payment_id: int, request: schema.PaymentUpdate, db: Session = Depends(get_db)):
	return controller.update(db=db, payment=request, payment_id=payment_id)


@router.delete("/{payment_id}")
def delete(payment_id: int, db: Session = Depends(get_db)):
	return controller.delete(db=db, payment_id=payment_id)


@router.get("/revenue/", response_model=schema.Revenue)
def get_revenue(start_date: str, end_date: str, db: Session = Depends(get_db)):
	return controller.get_revenue(db=db, start_date=start_date, end_date=end_date)
