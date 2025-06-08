from fastapi import APIRouter
from pydantic import BaseModel
from app.database import mongodb
from datetime import datetime

router = APIRouter(prefix="/consultations")

class Consultation(BaseModel):
    patient_email: str
    doctor: str
    diagnosis: str
    date: datetime

@router.post("/")
def add_consultation(consultation: Consultation):
    mongodb.consultations.insert_one(consultation.dict())
    return {"msg": "Consultation recorded"}

@router.get("/{email}")
def get_patient_history(email: str):
    history = list(mongodb.consultations.find({"patient_email": email}, {"_id": 0}))
    return history
