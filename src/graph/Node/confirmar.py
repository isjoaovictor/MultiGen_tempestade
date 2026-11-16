
from src.graph.state import State
from src.utils.mcp_client import get_tools_by_name, parse_result


async def confirmar(state: State) -> State:
    tools = await get_tools_by_name()

    raw = await tools["get_fleet_state"].ainvoke({})
    resultado = parse_result(raw)

    if "error" in resultado:
        return {
            "resultado": "erro_confirmacao",
            "erro": resultado["error"]
        }

    ship_id = state["ship_id"]
    velocidade_esperada = state["proposta"]["velocidade_kn"]

    for navio in resultado["navios"]:
        if navio["id"] == ship_id:

            if navio["velocidade_alvo_kn"] == velocidade_esperada:
                return {
                    "navio": navio,
                    "resultado": "concluido",
                    "erro": {}
                }

            return {
                "resultado": "erro_confirmacao",
                "erro": {
                    "code": "CONFIRMATION_FAILED",
                    "message": "A velocidade aplicada não corresponde à proposta"
                }
            }

    raise ValueError(f"Navio não encontrado: {ship_id}")
