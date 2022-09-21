from typing import List

from app.database.models import User
from app.shared.user_dto import UserDTO


class UserBuilder:
    @staticmethod
    def build(user: User) -> UserDTO:
        dto = UserDTO()
        dto.id = user.id
        dto.email = user.email
        dto.active = user.active
        return dto
    
    @staticmethod
    def build_all(users_db: List[User]) -> List[UserDTO]:
        users = [
            UserBuilder.build(user)
            for user in users_db
        ]
        return {
            'users': users
        }
