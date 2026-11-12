from typing import Annotated, TypedDict


class State(TypedDict, total=False):
    ship_id: str
    navio: dict
    proposta: dict
    revisao: dict
    rodada: int
    resultado: str 
    aprovado_operador: bool
    motivo_excecao: str

ESTADO_INICIAL: State = {
    "ship_id": "",
    "navio": "",
    "proposta": "",
    "revisao": "",
    "rodada": 0,
    "resultado": ""
}


