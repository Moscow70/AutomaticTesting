from typing import TypedDict, Annotated
from operator import add

def change_bar(state):
    return {"bar":["bye"]}

class State(TypedDict):
    foo : int
    bar : Annotated[list[str], add]

from langgraph.graph import StateGraph, END

graph = StateGraph(State)
graph.add_node("change_bar", change_bar)
graph.set_entry_point("change_bar")
graph.add_edge("change_bar", END)
app = graph.compile()

response = app.invoke({"foo":2, "bar":["hi"]})

print(response)