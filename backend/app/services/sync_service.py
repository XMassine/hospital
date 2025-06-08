from app.database import mongodb, neo4j_driver

def sync_patients():
    patients = mongodb.patients.find()
    with neo4j_driver.session() as session:
        for p in patients:
            session.run("""
                MERGE (p:Patient {email: $email})
                SET p.name = $name, p.age = $age
            """, name=p["name"], age=p["age"], email=p["email"])
