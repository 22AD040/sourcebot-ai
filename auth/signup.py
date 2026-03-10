from database.db import SessionLocal
from database.models import User
from auth.auth_utils import hash_password

def create_user(name, email, password):

    db = SessionLocal()

    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        return False

    new_user = User(
        name=name,
        email=email,
        password=hash_password(password)
    )

    db.add(new_user)
    db.commit()

    return True