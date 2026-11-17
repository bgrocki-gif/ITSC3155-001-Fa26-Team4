from typing import Optional
from pydantic import BaseModel
from .menu_item import MenuItem

class OrderItemBase(BaseModel):
    quantity: int
    subtotal: float

class OrderItemCreate(OrderItemBase):
    order_id: int
    item_id: int

class OrderItemUpdate(BaseModel):
    quantity: Optional[int] = None
    subtotal: Optional[float] = None

class OrderItem(OrderItemBase):
    order_item_id: int
    order_id: int
    item_id: int
    menu_item: Optional[MenuItem] = None

    class ConfigDict:
        from_attributes = True