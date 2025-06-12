from app.db.mongo import db
from app.db.neo4j import driver

def sync_data():
    patients = list(db.patients.find())
    medecins = list(db.medecins.find())
    with driver.session() as session:
        session.run("MATCH (p:Patient) DETACH DELETE p")
        for patient in patients:
            session.run("CREATE (:Patient {id: $id, nom: $nom})", id=patient["id"], nom=patient["nom"])
        session.run("MATCH (m:Medecin) DETACH DELETE m")
        for medecin in medecins:
            session.run("CREATE (:Medecin {id: $id, nom: $nom})", id=medecin["id"], nom=medecin["nom"])
