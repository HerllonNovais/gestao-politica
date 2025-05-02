from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth, eleitores, campanhas, whatsapp
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestão Política API",
    version="1.0",
    description="API para disparo de campanhas e gestão de eleitores",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Autenticação"])
app.include_router(eleitores.router, prefix="/api/eleitores", tags=["Eleitores"])
app.include_router(campanhas.router, prefix="/api/campanhas", tags=["Campanhas"])
app.include_router(whatsapp.router, prefix="/api/whatsapp", tags=["WhatsApp"])

@app.get("/")
def root():
    return {"status": "API em funcionamento"}
