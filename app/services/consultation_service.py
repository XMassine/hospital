from app.db.mongo import db
from app.models.consultation import Consultation

def ajouter_consultation(consult: Consultation):
    return db.consultations.insert_one(consult.dict())

def get_consultations_by_patient(patient_id: str):
    return list(db.consultations.find({"patient_id": patient_id}))