from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import bcrypt

from app.database.config import get_db
from app.repository import user_repository
from app.database.schemas import User, UserBase
from app.shared.builder import UserBuilder
from app.shared.inputs.create_user import CreateUserInput
from app.shared.inputs.update_user import UpdateUserInput

router = APIRouter()


@router.get('/user/all', tags=['users'])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users: List[User] = user_repository.find_all(db, skip, limit)
    return UserBuilder.build_all(users)


@router.get('/user/{user_id}', tags=['users'])
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user: User = user_repository.find_by_id(db, user_id)
    return UserBuilder.build(user)


@router.post('/user/register', tags=['users'], status_code=status.HTTP_201_CREATED)
async def save_user(user: CreateUserInput, db: Session = Depends(get_db)):
    user.password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_created = user_repository.save(db, user)
    return {'message': UserBuilder.build(user_created)}


@router.post('/user/{user_id}', tags=['users'])
async def update_user(user_id: int, user: UpdateUserInput, db: Session = Depends(get_db)):
    user_repository.update(db, user_id, user)
    return {'message': 'updated'}
