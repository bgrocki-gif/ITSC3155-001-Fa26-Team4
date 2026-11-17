from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, Text
from dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    item_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("menu_categories.category_id"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text,nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    available = Column(Boolean, nullable=False, default=True)