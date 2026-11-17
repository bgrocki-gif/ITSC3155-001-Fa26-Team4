from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base


class Menu(Base):
    __tablename__ = "menus"

    menu_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)