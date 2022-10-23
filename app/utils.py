from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)
    # hash is a pwd_context function that hashes the given password


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
    # verify is pwd_context function responsible for hashing and comparing hashed passwords!
