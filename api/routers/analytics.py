from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models.customer import Customer
from ..models.order import Order
from ..schemas.analytics import TopCustomer
from typing import List
from sqlalchemy import func, desc  

router = APIRouter(tags=["Top Customer Analysis"])
@router.get("/analytics/top-customers", response_model=List[TopCustomer], summary="Top 3 Customers by Spending")
def top_customers(db: Session = Depends(get_db)):
    try:
        results = (
            db.query(
                Customer.name,
                Customer.email,
                func.sum(Order.total).label("total_spent")  
            )
            .join(Order, Order.customer_id == Customer.id)
            .group_by(Customer.id)
            .order_by(desc("total_spent"))  
            .limit(3)
            .all()
        )
        return [
            {
                "name": r.name,
                "email": r.email,
                "total_spent": float(r.total_spent) if r.total_spent is not None else 0.0
            }
            for r in results
        ]
    except Exception as e:
        print(e)
        raise