from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.config import SessionLocal
from app.repository import user_repository
from app.database.schemas import UserBase

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/user/all', tags=['users'])
async def read_users(db: Session = Depends(get_db)):
    users = user_repository.find_all(db)
    return users


@router.post('/user/register', tags=['users'])
async def save_user(user: UserBase, db: Session = Depends(get_db)):
    user_repository.save(db, user)
    return {'message': 'ok'}
