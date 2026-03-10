from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE

engine = create_engine(
    DATABASE,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)