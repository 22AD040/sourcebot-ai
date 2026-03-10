from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password):
    password = str(password)[:72]
    return pwd_context.hash(password)

def verify_password(password, hashed):
    password = str(password)[:72]
    return pwd_context.verify(password, hashed)