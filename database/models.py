from sqlalchemy import Column, Integer, String, DateTime
from database.db import Base
import datetime


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


class Chat(Base):

    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    conversation_id = Column(String)
    role = Column(String)
    message = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)