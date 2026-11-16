from datetime import date
from typing import Optional
from pydantic import BaseModel

class ReviewBase(BaseModel):
    customer_id: int
    order_id: int
    review_text: Optional[str] = None
    score: int
    review_date: date

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[int] = None

class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True