from sqlalchemy.orm import Session
from models import Order
from schemas import OrderCreate
from typing import Optional


def create_order(db: Session, order_data: OrderCreate):
    new_order = Order(**order_data.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def update_order_status(db: Session, order_id: int, status: str):
    order = get_order(db, order_id)
    if order:
        order.status = status
        db.commit()
        db.refresh(order)
    return order

def get_orders(db: Session, status: Optional[str] = None):
    query = db.query(Order)
    if status:
        query = query.filter(Order.status == status)
    return query.all()
