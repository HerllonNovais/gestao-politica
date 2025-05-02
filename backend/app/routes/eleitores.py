from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Eleitor
from ..schemas import EleitorCreate

router = APIRouter()

@router.post("/")
def criar_eleitor(eleitor: EleitorCreate, db: Session = Depends(get_db)):
    db_eleitor = Eleitor(**eleitor.dict())
    db.add(db_eleitor)
    db.commit()
    return {"message": "Eleitor cadastrado com sucesso"}
