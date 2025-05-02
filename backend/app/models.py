from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String)
    nome = Column(String)
    ativo = Column(Boolean, default=True)

class Eleitor(Base):
    __tablename__ = "eleitores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    email = Column(String, nullable=True)
    endereco = Column(String, nullable=True)

class Campanha(Base):
    __tablename__ = "campanhas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    mensagem = Column(String)
    data_disparo = Column(DateTime)
    status = Column(String)  # agendada, enviada, cancelada
