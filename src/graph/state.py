from typing import TypedDict


class State(TypedDict, total=False):
    ship_id: str
    navio: dict
    proposta: dict
    revisao: dict

    rodada: int
    tentativas: int

    resultado: str
    resultado_execucao: dict

    aprovado_operador: bool
    motivo_excecao: str

    erro: dict
    idempotency_key: str


ESTADO_INICIAL: State = {
    "ship_id": "",
    "navio": {},
    "proposta": {},
    "revisao": {},
    "rodada": 0,
    "tentativas": 0,
    "resultado": "",
    "resultado_execucao": {},
    "aprovado_operador": False,
    "motivo_excecao": "",
    "erro": {},
    "idempotency_key": "",
}
