from graph.state import State
from langgraph.graph import END, START, StateGraph
from graph.routing import router_after_review
from langgraph.checkpoint.memory import InMemorySaver

from graph.Node.receive import receive
from graph.Node.navegador import navegador
from graph.Node.revisor import revisor
from graph.Node.escalar import escalar
from graph.Node.finalizar import finalizar


builder = StateGraph(State)

builder.add_node("receive", receive)
builder.add_node("navegador", navegador)
builder.add_node("revisor", revisor)
builder.add_node("escalar", escalar)
builder.add_node("finalizar", finalizar)

builder.add_edge(START, "receive")
builder.add_edge("receive", "navegador")
builder.add_edge("navegador", "revisor")
builder.add_conditional_edges(
    "revisor",
    router_after_review,{
        "aprovado": "finalizar",
        "tentar_de_novo": "navegador",
        "esgotado": "escalar"
    }
)
builder.add_edge("escalar", "finalizar")
builder.add_edge("finalizar", END)

graph = builder.compile(checkpointer=InMemorySaver())