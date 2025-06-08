from fastapi import APIRouter, Depends, HTTPException
from app.database import mongodb, neo4j_driver
from pydantic import BaseModel

router = APIRouter(prefix="/patients")

class Patient(BaseModel):
    name: str
    age: int
    email: str

@router.post("/")
def add_patient(patient: Patient):
    existing = mongodb.patients.find_one({"email": patient.email})
    if existing:
        raise HTTPException(status_code=400, detail="Patient already exists")
    
    mongodb.patients.insert_one(patient.dict())
    
    with neo4j_driver.session() as session:
        session.run("""
            CREATE (p:Patient {name: $name, age: $age, email: $email})
        """, name=patient.name, age=patient.age, email=patient.email)
    
    return {"msg": "Patient added successfully"}

@router.get("/")
def list_patients():
    patients = list(mongodb.patients.find({}, {"_id": 0}))
    return patients
