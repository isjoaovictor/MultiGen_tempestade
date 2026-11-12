from graph.state import State


def finalizar(state: State) -> State:
    id_navio = state["navio"]["id"]
    proposta = state["proposta"]
    rodada = state["rodada"]

    aprovacao = state.get("aprovado_operador")

    if proposta["acao"] == "NO_ACTION":
        mensagem = (f"Rodada {rodada}: O navegador não propôs nenhuma ação para o navio {id_navio}.")
    else:
        mensagem = (f"Rodada {rodada}: Velocidade {proposta['velocidade_kn']} nós aprovada para o navio {id_navio}.")

    if aprovacao is False:
        return {"resultado": f"\nRodada {rodada}: A proposta do navegador para o navio {id_navio} foi rejeitada pelo operador.\n"}
    if aprovacao is True:
        motivo = state.get("motivo_excecao", "")
        return {"resultado": f"\nRodada {rodada}: A proposta foi aprovada pelo operador como exceção à regra de segurança. O motivo informado foi “{motivo}”.\n"}


    return {"resultado": mensagem}