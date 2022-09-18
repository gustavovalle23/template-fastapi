from sqlalchemy.orm import Session

from app.database.models import User
from app.database.config import engine


class UserSeed:
    @staticmethod
    def insert_all():
        with Session(engine) as session:
            user_1 = User(
                email='admin@gmail.com',
                password='$2a$12$liEWsKidIhxfxne.g9s1wOrZFh/4KU2mmTLMN3NOa0rjL3797F942',  # admin
                active=True
            )
            user_2 = User(
                email='admin2@gmail.com',
                password='$2a$12$liEWsKidIhxfxne.g9s1wOrZFh/4KU2mmTLMN3NOa0rjL3797F942',  # admin
                active=True
            )
            session.add_all([user_1, user_2])
            session.commit()

    def remove_all():
        with Session(engine) as session:
            session.query(User).delete()
            session.commit()
