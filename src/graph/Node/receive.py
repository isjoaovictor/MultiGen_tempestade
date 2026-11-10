from graph.State import State
from dados import navios
import json
from pathlib import Path

for navio in navios:
    navio = navio

def receive(state: State) -> State:
    """carregar o navio pelo ship_id e retornar o estado atualizado"""
    ship_id = state["ship_id"]

    arquivo = Path(__file__).resolve().parents[2] / "dados" / "situacao_tempestade.json"
    dados = json.loads(arquivo.read_text(encoding="utf-8"))
    navios = dados["navios"]
    for navio in navios:
        if navio["id"] == ship_id:
            return {"navio": navio, "rodada": 0, "revisao": {}}

    raise ValueError(f"Navio não encontrado: {ship_id}")

   