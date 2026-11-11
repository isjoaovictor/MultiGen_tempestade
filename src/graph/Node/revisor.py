from pydantic import BaseModel
from graph.state import State
import json
from prompt.revisor_prompt import REVISOR_PROMPT
from utils.llm_adapter import get_llm

class Revisao(BaseModel):
    aprovado: bool
    motivo: str

def revisor(state: State) -> State:

    navio = state["navio"]
    proposta = state["proposta"]

    proposta_para_revisao = {
        "acao": proposta["acao"],
        "velocidade_kn": proposta["velocidade_kn"]
    }

    navio_json = json.dumps(navio, ensure_ascii=False)
    proposta_json = json.dumps(proposta_para_revisao, ensure_ascii=False)
    mensagens = REVISOR_PROMPT.format_messages(navio=navio_json, proposta=proposta_json)

    llm = get_llm().with_structured_output(Revisao)
    revisao = llm.invoke(mensagens)

    return {"revisao": revisao.model_dump()}