from sqlalchemy.orm import Session
from app.database import models
from app.database.schemas import UserBase


def find_all(db: Session):
    return db.query(models.User).all()


def save(db: Session, user: UserBase):
    user = models.User(email=user.email, password=user.password)
    db.add(user)
    db.commit()
    return user