from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.auth import hash_password, verify_password, create_access_token
from app.database import mongodb

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(user: User):
    if mongodb.users.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="User exists")
    user.password = hash_password(user.password)
    mongodb.users.insert_one(user.dict())
    return {"msg": "User created"}

@router.post("/login")
def login(user: User):
    db_user = mongodb.users.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token}
