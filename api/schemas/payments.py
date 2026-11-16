from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    order_id: int
    card_info: Optional[str] = None
    payment_type: str
    transaction_status: str = "PENDING"
    amount: float

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    card_info: Optional[str] = None
    payment_type: Optional[str] = None
    transaction_status: Optional[str] = None
    amount: Optional[float] = None

class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True