from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from ..database import SessionLocal
from ..models import Campanha
from ..schemas import CampanhaCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar_campanha(campanha: CampanhaCreate, db: Session = Depends(get_db)):
    db_campanha = Campanha(
        nome=campanha.nome,
        mensagem=campanha.mensagem,
        data_disparo=campanha.data_disparo,
        status="agendada"
    )
    db.add(db_campanha)
    db.commit()
    return {"message": "Campanha agendada com sucesso"}

@router.get("/")
def listar_campanhas(db: Session = Depends(get_db)):
    return db.query(Campanha).all()
