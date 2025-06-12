from app.db.mongo import db
from app.db.neo4j import driver

def authentifier(email: str, mot_de_passe: str):
    user = db.utilisateurs.find_one({"email": email, "mot_de_passe": mot_de_passe})
    if user:
        return user
    with driver.session() as session:
        result = session.run("""
            MATCH (u:Utilisateur {email: $email, mot_de_passe: $mot_de_passe}) RETURN u
        """, email=email, mot_de_passe=mot_de_passe)
        record = result.single()
        return record["u"] if record else None
