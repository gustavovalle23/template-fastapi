from typing import Optional
from sqlalchemy.orm import Session
from app.database.models import User
from app.database.schemas import UserBase


def find_all(db: Session):
    return db.query(User).filter(User.active == True).all()


def find_by_email(db: Session, email: str) -> User | None:
    user: Optional[User] = db.query(User).where(User.email == email)
    return user


def find_by_id(db: Session, user_id: int) -> User | None:
    user: Optional[User] = db.query(User).where(User.id == user_id)
    return user


def save(db: Session, user: UserBase):
    user = User(email=user.email, password=user.password)
    db.add(user)
    db.commit()
    return user


def update(db: Session, user_id: int, user: UserBase) -> None:
    db.query(User).filter(User.id == user_id).update(
        {'email': user.email, 'password': user.password}
    )
    db.commit()
