from pydantic import BaseModel

class Utilisateur(BaseModel):
    id: str
    nom: str
    email: str
    mot_de_passe: str
    role: str  # 'admin', 'medecin', 'patient'