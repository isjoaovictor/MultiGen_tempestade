from typing import Literal
from pydantic import BaseModel


class Proposta(BaseModel):
    """Proposta de ação do navegador para o revisor"""
    acao: Literal["SET_SPEED", "NO_ACTION"]
    velocidade_kn: float | None = None
    motivo: str
