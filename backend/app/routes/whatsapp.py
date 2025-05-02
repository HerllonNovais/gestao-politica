from fastapi import APIRouter, Depends, HTTPException
import requests
from ..config import EVOLUTION_API_URL

router = APIRouter()

@router.get("/qr-code")
def gerar_qrcode():
    try:
        response = requests.get(f"{EVOLUTION_API_URL}/qr-code")
        return {"qr_code": response.json().get("qrCode")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar QR Code: {str(e)}")

@router.post("/enviar-mensagem")
def enviar_mensagem(telefone: str, mensagem: str):
    try:
        response = requests.post(
            f"{EVOLUTION_API_URL}/send-message",
            json={"number": telefone, "text": mensagem}
        )
        return {"status": "mensagem enviada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar mensagem: {str(e)}")
