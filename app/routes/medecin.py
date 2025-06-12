from fastapi import APIRouter
from app.models.consultation import Consultation
from app.services.consultation_service import ajouter_consultation

router = APIRouter()

@router.post("/consultation")
def ajouter(consultation: Consultation):
    ajouter_consultation(consultation)
    return {"message": "Consultation enregistrée"}