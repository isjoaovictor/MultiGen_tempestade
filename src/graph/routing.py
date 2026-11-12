from graph.state import State

def router_after_review(state: State) -> str:
    if state["revisao"]["aprovado"]:
        return ("aprovado").lower()
    elif state["revisao"]["aprovado"] is False and state["rodada"] == 1:
        return "tentar_de_novo"
    elif state["revisao"]["aprovado"] is False and state["rodada"] == 2:
        return "esgotado"



        