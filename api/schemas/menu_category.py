from typing import Optional
from pydantic import BaseModel, ConfigDict

class MenuCategoryBase(BaseModel):
    menu_id: int
    name: str

class MenuCategoryCreate(MenuCategoryBase):
    pass

class MenuCategoryUpdate(BaseModel):
    menu_id: Optional[int] = None
    name: Optional[str] = None

class MenuCategory(MenuCategoryBase):
    category_id: int

    class ConfigDict:
        from_attributes = True

