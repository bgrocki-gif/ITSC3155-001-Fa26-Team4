from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    promo_id = Column(Integer, ForeignKey("promotions.promo_id"), nullable=True)
    order_date = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)
    order_type = Column(String(50), nullable=False)
    total = Column(Numeric(8,2), nullable=False)
    tracking_number = Column(String(100), unique=True, nullable=False)


