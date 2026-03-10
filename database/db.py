from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE

engine = create_engine(DATABASE)

SessionLocal = sessionmaker(bind=engine)