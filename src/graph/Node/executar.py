import os

from src.graph.state import State
from src.utils.mcp_client import get_tools_by_name, parse_result


def simular_conflito_ativo() -> bool:
    """True se a variável de ambiente SIMULAR_CONFLITO for 1/true/yes/on."""
    return os.getenv("SIMULAR_CONFLITO", "").strip().lower() in {"1", "true", "yes", "on"}


async def executar(state: State) -> State:
    tools = await get_tools_by_name()

    navio = state["navio"]
    proposta = state["proposta"]

    tentativas = state.get("tentativas", 0)

    versao = navio["state_version"]

    expected_version = versao

    # Teste de recuperação: na 1ª tentativa envia uma versão velha de propósito
    if tentativas == 0 and simular_conflito_ativo():
        expected_version = versao - 1
        print(f"[SIMULAR_CONFLITO] enviando expected_state_version={expected_version} (real={versao})")

    velocidade = proposta["velocidade_kn"]
    ship_id = state["ship_id"]

    chave = state.get("idempotency_key") or (
        f"treino:{ship_id}:SET_SPEED:v{versao}"
    )

    raw = await tools["set_speed"].ainvoke({
        "ship_id": ship_id,
        "speed_kn": velocidade,
        "expected_state_version": expected_version,
        "idempotency_key": chave,
    })

    resultado = parse_result(raw)

    if "error" in resultado:
        return {
            "resultado_execucao": resultado,
            "erro": resultado["error"],
            "tentativas": tentativas + 1,
        }

    return {
        "resultado_execucao": resultado,
        "erro": {},
        "tentativas": tentativas + 1,
        "resultado": "executado",
    }
