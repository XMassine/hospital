from pydantic import BaseModel

class Consultation(BaseModel):
    id: str
    date: str
    motif: str
    medecin_id: str
    patient_id: str
