from src.graph.state import State


def validar(state: State) -> State:
    proposta = state["proposta"]

    if proposta["acao"] == "NO_ACTION":
        return {
            "resultado": "sem_acao",
            "erro": {}
        }

    velocidade = proposta.get("velocidade_kn")

    if (
        not isinstance(velocidade, (int, float))
        or isinstance(velocidade, bool)
        or not 0 <= velocidade <= 18
        or velocidade * 2 != int(velocidade * 2)
    ):
        return {
            "resultado": "invalido",
            "erro": {
                "code": "INVALID_SCHEMA",
                "message": "Velocidade inválida"
            }
        }

    return {
        "resultado": "validado",
        "erro": {}
    }
