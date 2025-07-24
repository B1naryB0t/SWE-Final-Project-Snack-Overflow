from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import customer as controller
from ..dependencies.database import get_db
from ..schemas import customer as schema

router = APIRouter(
    tags=['Customers'],
    prefix="/customer"
)


@router.post("/", response_model=schema.Customer)
def create(request: schema.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, customer=request)


@router.get("/", response_model=list[schema.Customer])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{customer_id}", response_model=schema.Customer)
def read_one(customer_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, customer_id=customer_id)


@router.put("/{customer_id}", response_model=schema.Customer)
def update(customer_id: int, request: schema.CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, customer=request, customer_id=customer_id)


@router.delete("/{customer_id}")
def delete(customer_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, customer_id=customer_id)
