from sqlalchemy import Column, Integer, ForeignKey, Text, Date
from dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=True)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=True)
    date = Column(Date, nullable=False)