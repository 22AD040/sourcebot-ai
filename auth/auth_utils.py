from passlib.hash import bcrypt

def hash_password(password):

    password = str(password)[:72]

    return bcrypt.hash(password)


def verify_password(password, hashed):

    password = str(password)[:72]

    return bcrypt.verify(password, hashed)