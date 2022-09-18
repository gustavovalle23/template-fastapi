from pydantic import BaseModel

class UpdateUserInput(BaseModel):
    email: str
    active: bool = True
