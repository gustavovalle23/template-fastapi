from fastapi import FastAPI
from .routers import users
from app.database import models
from app.database.config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(users.router)
