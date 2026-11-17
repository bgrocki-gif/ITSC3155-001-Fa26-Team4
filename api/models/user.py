from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=True)
    address = Column(String(100), nullable=True)