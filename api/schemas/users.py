from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    role: str = "customer"
    phone: Optional[str] = None
    address: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class User(UserBase):
    user_id: int

    class ConfigDict:
        from_attributes = True