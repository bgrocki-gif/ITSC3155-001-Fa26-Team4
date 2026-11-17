from typing import Optional
from pydantic import BaseModel
from .menu_item import MenuItem

class ResourceBase(BaseModel):
    name: str
    quantity: float
    unit: str

class ResourceCreate(ResourceBase):
    pass

class ResourceUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[float] = None
    unit: Optional[str] = None

class Resource(ResourceBase):
    resource_id: int

    class ConfigDict:
        from_attributes = True