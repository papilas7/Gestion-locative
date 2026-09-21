from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware # <-- 1. Importer le CORS
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, get_db

# Création automatique des tables SQLite au démarrage
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="MVP Gestion Locative")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # L'étoile (*) signifie "J'autorise tout le monde". Idéal pour le MVP.
    allow_credentials=True,
    allow_methods=["*"],  # Autorise les requêtes GET, POST, PUT, DELETE...
    allow_headers=["*"],  # Autorise tous les types de données envoyées
)
# Schemas Pydantic pour valider les données envoyées par le front-end
class BienCreate(BaseModel):
    code_ref: str
    type_bien: str
    loyer_hc: float
    charges: float = 0.0

class LocataireCreate(BaseModel):
    nom: str
    prenom: str
    telephone: str

class PaiementCreate(BaseModel):
    contrat_id: int
    montant: float
    mois: str
    mode_paiement: str

# Routes de l'API
@app.post("/biens/")
def ajouter_bien(bien: BienCreate, db: Session = Depends(get_db)):
    db_bien = models.Bien(**bien.dict())
    db.add(db_bien)
    db.commit()
    db.refresh(db_bien)
    return db_bien

@app.get("/biens/")
def lister_biens(db: Session = Depends(get_db)):
    return db.query(models.Bien).all()

@app.post("/locataires/")
def ajouter_locataire(locataire: LocataireCreate, db: Session = Depends(get_db)):
    db_loc = models.Locataire(**locataire.dict())
    db.add(db_loc)
    db.commit()
    db.refresh(db_loc)
    return db_loc

@app.get("/locataires/")
def lister_locataires(db: Session = Depends(get_db)):
    return db.query(models.Locataire).all()

@app.post("/paiements/")
def enregistrer_paiement(paiement: PaiementCreate, db: Session = Depends(get_db)):
    db_pay = models.Paiement(**paiement.dict())
    db.add(db_pay)
    db.commit()
    db.refresh(db_pay)
    return db_pay