from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Patient"])

# ✅ Liste complète des consultations simulées
consultations_fictives = [
    {"id": "c001", "patient_id": "pat001", "medecin_id": "med001", "date": "2025-06-01", "description": "Consultation 1"},
    {"id": "c002", "patient_id": "pat002", "medecin_id": "med001", "date": "2025-06-02", "description": "Consultation 2"},
    {"id": "c003", "patient_id": "pat002", "medecin_id": "med002", "date": "2025-06-03", "description": "Consultation 3"},
    {"id": "c004", "patient_id": "pat003", "medecin_id": "med001", "date": "2025-06-04", "description": "Consultation 4"},
    {"id": "c005", "patient_id": "pat003", "medecin_id": "med002", "date": "2025-06-05", "description": "Consultation 5"},
    {"id": "c006", "patient_id": "pat003", "medecin_id": "med003", "date": "2025-06-06", "description": "Consultation 6"},
    {"id": "c007", "patient_id": "pat003", "medecin_id": "med001", "date": "2025-06-07", "description": "Consultation 7"},
]

@router.get("/patient/historique/{patient_id}")
def get_historique(patient_id: str):
    resultats = [c for c in consultations_fictives if c["patient_id"] == patient_id]
    if not resultats:
        raise HTTPException(status_code=404, detail="Aucune consultation trouvée pour ce patient")
    return resultats
