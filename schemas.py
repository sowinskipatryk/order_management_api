from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    customer_name: str
    total_amount: float
    currency: str

class OrderUpdate(BaseModel):
    status: str

class OrderResponse(BaseModel):
    id: int
    customer_name: str
    total_amount: float
    currency: str
    converted_amount: Optional[float] = None
    status: str

    class Config:
        from_attributes = True
