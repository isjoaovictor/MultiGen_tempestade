from langgraph.graph import END, START, StateGraph
from langgraph.checkpoint.memory import InMemorySaver

from src.graph.state import State
from src.graph.routing import (
    router_after_review,
    route_after_validate,
    route_after_execute,
)

from src.graph.Node.ler_estado import ler_estado
from src.graph.Node.navegador import navegador
from src.graph.Node.revisor import revisor
from src.graph.Node.validar import validar
from src.graph.Node.executar import executar
from src.graph.Node.confirmar import confirmar
from src.graph.Node.escalar import escalar
from src.graph.Node.finalizar import finalizar


builder = StateGraph(State)

# Registro dos nós
builder.add_node("ler_estado", ler_estado)
builder.add_node("navegador", navegador)
builder.add_node("revisor", revisor)
builder.add_node("validar", validar)
builder.add_node("executar", executar)
builder.add_node("confirmar", confirmar)
builder.add_node("escalar", escalar)
builder.add_node("finalizar", finalizar)

# Fluxo inicial
builder.add_edge(START, "ler_estado")
builder.add_edge("ler_estado", "navegador")
builder.add_edge("navegador", "revisor")

# Decisão do revisor
builder.add_conditional_edges(
    "revisor",
    router_after_review,
    {
        "aprovado": "validar",
        "tentar_de_novo": "navegador",
        "esgotado": "escalar",
    }
)

# Decisão da validação
builder.add_conditional_edges(
    "validar",
    route_after_validate,
    {
        "executar": "executar",
        "finalizar": "finalizar",
    }
)

# Decisão da execução
builder.add_conditional_edges(
    "executar",
    route_after_execute,
    {
        "confirmar": "confirmar",
        "reler_estado": "ler_estado",
        "falha": "finalizar",
    }
)

# Encerramento
builder.add_edge("confirmar", "finalizar")
builder.add_edge("escalar", "finalizar")
builder.add_edge("finalizar", END)

graph = builder.compile(checkpointer=InMemorySaver())
