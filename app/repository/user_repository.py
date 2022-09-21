import random
import string
from typing import Optional
from sqlalchemy.orm import Session
from app.database.models import User
from app.shared.inputs.create_user import CreateUserInput
from app.shared.inputs.update_user import UpdateUserInput


def find_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).filter(User.active == True).offset(skip).limit(limit)


def find_by_email(db: Session, email: str) -> User | None:
    user: Optional[User] = db.query(User).where(User.email == email)
    return user


def find_by_id(db: Session, user_id: int) -> User | None:
    user = db.query(User).filter(User.id == user_id).filter(User.active == True).first()
    return user


def save(db: Session, user: CreateUserInput):
    user = User(email=user.email, password=user.password)
    db.add(user)
    db.commit()
    return user


def update(db: Session, user_id: int, user: UpdateUserInput) -> None:
    db.query(User).filter(User.id == user_id).update(
        {'email': user.email, 'active': user.active}
    )
    db.commit()


def inactivate(db: Session, user_id: int) -> None:
    db.query(User).filter(User.id == user_id).update(
        {'active': False}
    )
    db.commit()


def delete(db: Session, user_id: int) -> None:
    db.query(User).filter(User.id == user_id).update(
        {'email': random_string(), 'active': False, 'password': random_string()}
    )
    db.commit()


def random_string():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
