from app.models.utilisateur import Utilisateur

class Medecin(Utilisateur):
    specialite: str
