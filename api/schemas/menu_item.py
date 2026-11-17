from typing import Optional
from pydantic import BaseModel

class MenuItemBase(BaseModel):
    category_id: int
    name: str
    description: str
    price: float
    available: bool = True

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    category_id: int
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    available: Optional[bool] = None

class MenuItem(MenuItemBase):
    item_id: int

    class ConfigDict:
        from_attributes = True