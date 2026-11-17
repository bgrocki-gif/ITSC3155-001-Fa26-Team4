from datetime import date
from typing import Optional
from pydantic import BaseModel

class ReviewBase(BaseModel):
    user_id: int
    order_id: int
    rating: int
    comment: Optional[str] = None
    date: date

class ReviewCreate(ReviewBase):
    pass

class ReviewUpdate(BaseModel):
    rating: Optional[int] = None
    comment: Optional[str] = None

class Review(ReviewBase):
    review_id: int

    class ConfigDict:
        from_attributes = True