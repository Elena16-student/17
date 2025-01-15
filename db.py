from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.sql.functions import session_user
from sqlalchemy import Column, Integer, String

enjine = create_engine('sqlite:///taskmanager.db', echo=True)
SessionLocal = sessionmaker (bind=enjine)

class Base(DeclarativeBase):
    pass

