from typing import Optional
from pydantic import BaseModel, ConfigDict

class MenuBase(BaseModel):
    name: str

class MenuCreate(MenuBase):
    pass

class MenuUpdate(BaseModel):
    name: Optional[str] = None

class Menu(MenuBase):
    menu_id: int

    class ConfigDict:
        from_attributes = True

