from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import models
from app.database.config import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(db: Session):
    return db.query(models.User).all()


@router.get('/users/', tags=['users'])
async def read_users(db: Session = Depends(get_db)):
    users = get_user(db)
    return users
