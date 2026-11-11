from graph.state import State
from langgraph.graph import END, START, StateGraph



builder = StateGraph(State)

builder.add_node("receive", receive)
builder.add_node("navegador", navegador)
builder.add_node("revisor", revisor)
builder.add_node("escalar", escalar)
builder.add_node("finalizar", finalizar)