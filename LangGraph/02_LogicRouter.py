# router() checks word count: < 4 words → "clarify", else → "generate"
# add_conditional_edges maps router return values to node names
# Interactive loop keeps the chatbot running until user types "salir"

from typing import TypedDict


# ── Estado ──────────────────────────────────────────────
class State(TypedDict):
    text: str
    response: str


# ── Modelo (asegúrate de tener ollama corriendo) ────────
# Definimos el modelo que vamos a usar
model_name = "gpt-oss:20b"
model = ChatOllama(model=model_name, temperature=0)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer in the same language the user writes.",
        ),
        ("human", "{text}"),
    ]
)


# ── Nodos ───────────────────────────────────────────────
def generate(state: State) -> State:
    chain = prompt | model
    result = chain.invoke({"text": state["text"]})
    return {"response": result.content}


def clarify(_: State) -> State:
    return {"response": "Por favor, elabora más tu pregunta (mínimo 4 palabras)."}


def router(state: State) -> str:
    if len(state["text"].split()) < 4:
        return "clarify"
    return "generate"


# ── Grafo ───────────────────────────────────────────────
graph = StateGraph(State)
graph.add_node("router", lambda state: state)
graph.add_node("generate", generate)
graph.add_node("clarify", clarify)
graph.add_edge(START, "router")
graph.add_conditional_edges(
    "router", router, {"generate": "generate", "clarify": "clarify"}
)

app = graph.compile()

# ── Loop interactivo ────────────────────────────────────
print("Chatbot listo. Escribe 'salir' para terminar.\n")
while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        break
    result = app.invoke({"text": user_input})
    print(f"Bot: {result['response']}\n")
