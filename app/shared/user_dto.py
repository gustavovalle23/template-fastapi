from app.database.schemas import User


class UserDTO:
    email: str

    def __init__(self, user: User) -> None:
        self.email = user.email

def convert(user: User):
    return UserDTO(user)
