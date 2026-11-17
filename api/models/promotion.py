from sqlalchemy import Column, Integer, String, Numeric, DateTime
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    promo_id = Column(Integer, primary_key=True, index=True)
    promo_code = Column(String(100), unique=True, nullable=False)
    discount_percent = Column(Numeric(5,2), nullable=False)
    expiry_date = Column(DateTime, nullable=False)





