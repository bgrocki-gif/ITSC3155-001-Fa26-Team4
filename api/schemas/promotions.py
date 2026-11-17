from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PromotionBase(BaseModel):
    promo_code: str
    discount_percent: float
    expiration_date: datetime

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    promo_code: Optional[str] = None
    discount_percent: Optional[float] = None
    expiration_date: Optional[datetime] = None

class Promotion(PromotionBase):
    promo_id: int

    class ConfigDict:
        from_attributes = True