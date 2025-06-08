from passlib.context import CryptContext
from app.database import mongodb

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(email: str, password: str, role: str):
    if mongodb.users.find_one({"email": email}):
        raise Exception("User already exists")
    
    hashed_password = pwd_context.hash(password)
    mongodb.users.insert_one({
        "email": email,
        "password": hashed_password,
        "role": role
    })
    return {"msg": "User created"}

def authenticate_user(email: str, password: str):
    user = mongodb.users.find_one({"email": email})
    if not user:
        return False
    if not pwd_context.verify(password, user["password"]):
        return False
    return user
