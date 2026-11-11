from typing import Literal
from graph import state
from pydantic import BaseModel
from graph.state import State
import json
from prompt.navegador_prompt import NAVEGADOR_PROMPT
from utils.llm_adapter import get_llm


class Proposta(BaseModel):
    """Proposta de ação do navegador para o revisor"""
    acao: Literal["SET_SPEED", "NO_ACTION"]
    velocidade_kn: float | None = None
    motivo: str

def navegador(state: State) -> State:
    """Função que representa o nó do navegador no grafo de estados"""

    feedback = ""
    aprovado = state["revisao"].get("aprovado")
    if aprovado is False:
        feedback = state["revisao"]["motivo"]
    navio = state["navio"]
    navio_json = json.dumps(navio, ensure_ascii=False)

    mensagens = NAVEGADOR_PROMPT.format_messages(navio=navio_json, feedback=feedback)
    llm = get_llm().with_structured_output(Proposta)
    proposta = llm.invoke(mensagens)

    return {"rodada": state["rodada"] + 1, "proposta": proposta.model_dump()}

        