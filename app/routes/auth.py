from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db.mongo import db

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    user = db["users"].find_one({"email": data.email, "password": data.password})
    if user:
        return {
            "id": user["id"],
            "email": user["email"],
            "role": user["role"]
        }
    raise HTTPException(status_code=401, detail="Email ou mot de passe invalide")
