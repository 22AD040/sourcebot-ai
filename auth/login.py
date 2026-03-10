from database.db import SessionLocal
from database.models import User
from auth.auth_utils import verify_password

def login_user(email, password):

    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if user and verify_password(password, user.password):
        return user

    return None