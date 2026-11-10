from typing import Annotated, TypedDict
from langgraph.graph import add_messages

class State(TypedDict, total=False):
    ship_id: str
    navio: str
    proposta: str
    revisao: str
    rodada: str
    resultado: str 

ESTADO_INICIAL: State = (
    "ship_id": "",
    "navio": "",
    "proposta": "",
    "revisao": "",
    "rodada": "",
    "resultado": ""

)


