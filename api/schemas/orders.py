from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail

class OrderBase(BaseModel):
    customer_id: int
    promo_id: Optional[int] = None
    tracking_number: str
    order_status: str = "PLACED"
    order_type: str = "TAKEOUT"
    total_price: float = 0.0
    description: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    promo_id: Optional[int] = None
    order_status: Optional[str] = None
    order_type: Optional[str] = None
    total_price: Optional[float] = None
    description: Optional[str] = None

class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = []

    class ConfigDict:
        from_attributes = True
