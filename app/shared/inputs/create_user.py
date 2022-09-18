from pydantic import BaseModel


class CreateUserInput(BaseModel):
    email: str
    active: bool = True
    password: str
