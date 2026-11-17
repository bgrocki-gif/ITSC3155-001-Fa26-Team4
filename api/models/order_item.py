from sqlalchemy import Column, Integer, ForeignKey, Numeric
from ..dependencies.database import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    item_id = Column(Integer, ForeignKey("menu_items.item_id"), nullable=True)
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Numeric(10, 2), nullable=False)