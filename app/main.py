from fastapi import FastAPI
from app.routes import auth, admin, medecin, patient
from fastapi.middleware.cors import CORSMiddleware






app = FastAPI()

# ✅ CORS activé avant les routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # autoriser Angular
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Inclusion des routes (une seule fois !)
app.include_router(auth.router)

app.include_router(patient.router)


app.include_router(admin.router, prefix="/admin")
app.include_router(medecin.router, prefix="/medecin")












@app.get("/")
def read_root():
    return {"message": "Cabinet Médical API"}