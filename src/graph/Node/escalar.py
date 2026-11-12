from graph.state import State

from langgraph.types import interrupt

def escalar(state: State) -> State:
   acao = state["proposta"]["acao"]
   velocidade = state["proposta"]["velocidade_kn"]
   motivo = state["proposta"]["motivo"]
   motivo_rejeicao = state["revisao"]["motivo"]
   dados_revisao = {
        "id_navio": state["navio"]["id"],
        "acao": acao,
        "velocidade_kn": velocidade,
        "motivo": motivo,
        "motivo_rejeicao": motivo_rejeicao
        }
   aprovacao = interrupt(dados_revisao)


   return {"aprovado_operador": aprovacao}
