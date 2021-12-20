from sqlalchemy import create_engine
from dotenv import dotenv_values
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

envs = dotenv_values('.env')

engine = create_engine(envs['DATABASE_URL'])
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
