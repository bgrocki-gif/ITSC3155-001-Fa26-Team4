from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_item import OrderItem

class OrderBase(BaseModel):
    customer_id: Optional[int] = None
    promo_id: Optional[int] = None
    tracking_number: str
    status: str = "PLACED"
    order_type: str = "TAKEOUT"
    total: float = 0.0

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    promo_id: Optional[int] = None
    status: Optional[str] = None
    order_type: Optional[str] = None
    total: Optional[float] = None

class Order(OrderBase):
    order_id: int
    order_date: datetime
    order_details: list[OrderItem] = []

    class ConfigDict:
        from_attributes = True
