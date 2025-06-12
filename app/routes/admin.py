from fastapi import APIRouter
from app.db.mongo import db
from app.db.neo4j import driver

router = APIRouter()

@router.post("/medecin")
def ajouter_medecin(data: dict):
    db.medecins.insert_one(data)
    with driver.session() as session:
        session.run("CREATE (:Medecin {id: $id, nom: $nom})", id=data["id"], nom=data["nom"])
    return {"message": "Médecin ajouté"}

@router.post("/patient")
def ajouter_patient(data: dict):
    db.patients.insert_one(data)
    with driver.session() as session:
        session.run("CREATE (:Patient {id: $id, nom: $nom})", id=data["id"], nom=data["nom"])
    return {"message": "Patient ajouté"}