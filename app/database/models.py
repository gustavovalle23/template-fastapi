from sqlalchemy import Integer, Column, String, Boolean
from .config import Base


class User(Base):
    __tablename__ = "user"

    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String(255), unique=True, nullable=False)
    password: str = Column(String(255))
    active: bool = Column(Boolean(), default=True)
