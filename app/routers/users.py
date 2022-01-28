from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.config import SessionLocal
from app.repository import user_repository
from app.database.schemas import User, UserBase
from app.shared.authentication_dto import AuthDTO
from app.service import user_service
from app.shared.user_dto import UserDTO, convert

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/user/all', tags=['users'])
async def read_users(db: Session = Depends(get_db)):
    users: List[User] = user_repository.find_all(db)
    users_dto: List[UserDTO] = [convert(user) for user in users]

    return users_dto


@router.post('/user/register', tags=['users'])
async def save_user(user: UserBase, db: Session = Depends(get_db)):
    user_repository.save(db, user)
    return {'message': 'ok'}


@router.post('/user/authenticate', tags=['user'])
async def authenticate(authentication_dto: AuthDTO):
    user_service.authenticate(authentication_dto)
