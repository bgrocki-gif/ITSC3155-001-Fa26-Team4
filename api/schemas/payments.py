from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    order: int
    amount: float
    method: str
    card_info: Optional[str] = None
    status: str = "PENDING"


class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    card_info: Optional[str] = None
    method: Optional[str] = None
    status: Optional[str] = None
    amount: Optional[float] = None

class Payment(PaymentBase):
    payment_id: int

    class ConfigDict:
        from_attributes = True