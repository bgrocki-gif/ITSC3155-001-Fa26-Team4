from typing import Optional
from pydantic import BaseModel

class MenuItemBase(BaseModel):
    category_id: int
    name: str
    ingredients: str
    description: Optional[str] = None
    price: float
    calories: int
    available: bool = True

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    ingredients: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    available: Optional[bool] = None

class MenuItem(MenuItemBase):
    item_id: int

    class ConfigDict:
        from_attributes = True