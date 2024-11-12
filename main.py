from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from database import init_db, get_db
from typing import Optional
from schemas import OrderCreate, OrderUpdate, OrderResponse
from crud import create_order, get_order, update_order_status, get_orders
from currency import get_exchange_rate


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = await init_db()
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.post("/orders/", response_model=OrderResponse)
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = create_order(db, order)
    return db_order

@app.put("/orders/{order_id}", response_model=OrderResponse)
def update_order_status_endpoint(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    order = update_order_status(db, order_id, order_update.status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/orders/{order_id}", response_model=OrderResponse)
def get_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    order = get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    exchange_rate = get_exchange_rate(order.currency)
    if exchange_rate is not None:
        order.converted_amount = order.total_amount * exchange_rate
    return order

@app.get("/orders/", response_model=list[OrderResponse])
def list_orders(status: Optional[str] = None, db: Session = Depends(get_db)):
    return get_orders(db, status)
