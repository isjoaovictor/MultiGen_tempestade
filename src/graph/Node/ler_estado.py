
from src.graph.state import State
from src.utils.mcp_client import get_tools_by_name, parse_result


async def ler_estado(state: State) -> State:
    """Consulta o estado da frota pelo servidor MCP."""

    tools = await get_tools_by_name()

    resultado = await tools["get_fleet_state"].ainvoke({})

    resultado = parse_result(resultado)

    if "error" in resultado:
        raise RuntimeError(resultado["error"])

    ship_id = state["ship_id"]

    for navio in resultado["navios"]:
        if navio["id"] == ship_id:
            return {
                "navio": navio,
                "rodada": state.get("rodada", 0),
                "tentativas": state.get("tentativas", 0),
                "revisao": {},
                "resultado_execucao": None,
            }

    raise ValueError(f"Navio não encontrado: {ship_id}")
