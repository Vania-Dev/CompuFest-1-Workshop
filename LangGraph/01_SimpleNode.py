# Defines a TypedDict State with text and response fields
# Single "generate" node invokes the LLM and writes to state["response"]
# set_entry_point and set_finish_point mark the only node as start and end

from typing import TypedDict

# Definimos el modelo que vamos a usar
model_name = "gpt-oss:20b"

llm = ChatOllama(model=model_name, temperature=0)


class State(TypedDict):
    text: str
    response: str


def generate(state: State) -> State:
    result = llm.invoke(state["text"])
    return {"response": result.content}


graph = StateGraph(State)
graph.add_node("generate", generate)
graph.set_entry_point("generate")
graph.set_finish_point("generate")

app = graph.compile()
output = app.invoke({"text": "Explain LangGraph in one sentence"})
print(output["response"])
