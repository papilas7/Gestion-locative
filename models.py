from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Bien(Base):
    __tablename__ = "biens"

    id = Column(Integer, primary_key=True, index=True)
    code_ref = Column(String, unique=True, index=True) # ex: "APP-101"
    type_bien = Column(String)                         # Appartement, Studio, Magasin
    loyer_hc = Column(Float)
    charges = Column(Float, default=0.0)
    statut = Column(String, default="Disponible")      # Disponible, Loué

    contrats = relationship("Contrat", back_populates="bien")


class Locataire(Base):
    __tablename__ = "locataires"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    prenom = Column(String)
    telephone = Column(String)

    contrats = relationship("Contrat", back_populates="locataire")


class Contrat(Base):
    __tablename__ = "contrats"

    id = Column(Integer, primary_key=True, index=True)
    bien_id = Column(Integer, ForeignKey("biens.id"))
    locataire_id = Column(Integer, ForeignKey("locataires.id"))
    loyer_total = Column(Float)
    statut = Column(String, default="Actif")

    bien = relationship("Bien", back_populates="contrats")
    locataire = relationship("Locataire", back_populates="contrats")
    paiements = relationship("Paiement", back_populates="contrat")


class Paiement(Base):
    __tablename__ = "paiements"

    id = Column(Integer, primary_key=True, index=True)
    contrat_id = Column(Integer, ForeignKey("contrats.id"))
    montant = Column(Float)
    mois = Column(String)                              # ex: "09/2026"
    mode_paiement = Column(String)                     # Espèces, Mobile Money, Virement

    contrat = relationship("Contrat", back_populates="paiements")