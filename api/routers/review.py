from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import review as controller
from ..dependencies.database import get_db
from ..schemas import review as schema

router = APIRouter(
    tags=['Reviews'],
    prefix="/review"
)


@router.post("/", response_model=schema.Review)
def create(request: schema.ReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, review=request)


@router.get("/", response_model=list[schema.Review])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{review_id}", response_model=schema.Review)
def read_one(review_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, review_id=review_id)


@router.put("/{review_id}", response_model=schema.Review)
def update(review_id: int, request: schema.ReviewUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, review=request, review_id=review_id)


@router.delete("/{review_id}")
def delete(review_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, review_id=review_id)
