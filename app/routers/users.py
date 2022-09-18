from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.repository import user_repository
from app.database.schemas import User, UserBase
from app.shared.user_dto import UserDTO, convert

router = APIRouter()


@router.get('/user/all', tags=['users'])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users: List[User] = user_repository.find_all(db, skip, limit)
    users_dto: List[UserDTO] = [convert(user) for user in users]
    return users_dto


@router.post('/user/register', tags=['users'])
async def save_user(user: UserBase, db: Session = Depends(get_db)):
    user_repository.save(db, user)
    return {'message': 'ok'}
