from pydantic import BaseModel, Field
from datetime import datetime

# Usuários
class UsuarioCreate(BaseModel):
    email: str
    senha: str = Field(min_length=6)
    nome: str

# Eleitores
class EleitorCreate(BaseModel):
    nome: str
    telefone: str = Field(regex=r"^\d{10,11}$")
    email: str | None = None

# Campanhas
class CampanhaCreate(BaseModel):
    nome: str
    mensagem: str
    data_disparo: datetime
