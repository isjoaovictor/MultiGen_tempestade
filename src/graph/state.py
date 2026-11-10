from typing import Annotated, TypedDict
from langgraph.graph import add_messages

class State(TypedDict, total=False):
    ship_id: str
    navio: dict
    proposta: dict
    revisao: dict
    rodada: int
    resultado: str 

ESTADO_INICIAL: State = {
    "ship_id": "",
    "navio": "",
    "proposta": "",
    "revisao": "",
    "rodada": 0,
    "resultado": ""
}


