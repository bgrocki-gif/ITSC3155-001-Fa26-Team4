from sqlalchemy import Column, Integer, String, ForeignKey
from ..dependencies.database import Base


class MenuCategory(Base):
    __tablename__ = "menu_categories"

    category_id = Column(Integer, primary_key=True, index=True)
    menu_id = Column(Integer, ForeignKey("menus.menu_id"), nullable=False)
    name = Column(String(100), nullable=False)