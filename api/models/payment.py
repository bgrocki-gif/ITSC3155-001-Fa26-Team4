from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    order= Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    method = Column(String(100), nullable=False)
    card_info = Column(String(100), nullable=True)
    status = Column(String(100), nullable=False)
