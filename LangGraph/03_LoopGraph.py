# iterations counter in State tracks how many review passes have run
# should_continue() routes back to "review" until MAX_ITERATIONS is reached
# Demonstrates a self-improvement loop: generate → review → review → ... → END

from typing import TypedDict


# ── Estado ──────────────────────────────────────────────
class State(TypedDict):
    text: str
    response: str
    iterations: int  # contador de mejoras


# ── Modelo ──────────────────────────────────────────────
model_name = "gpt-oss:20b"
llm = ChatOllama(model=model_name, temperature=0)

MAX_ITERATIONS = 3  # cuántas veces mejorar la respuesta


# ── Nodo 1: Genera respuesta inicial ────────────────────
def generate(state: State) -> State:
    print("📝 Generando respuesta inicial...")
    prompt = f"Answer this question briefly:\n{state['text']}"
    result = llm.invoke(prompt)
    print(f"   Respuesta: {result.content}\n")
    return {"response": result.content, "iterations": 0}


# ── Nodo 2: Mejora la respuesta ──────────────────────────
def review(state: State) -> State:
    iteration = state["iterations"] + 1
    print(f"✨ Mejora #{iteration}...")
    prompt = (
        f"Improve this answer, make it clearer and more complete:\n{state['response']}"
    )
    improved = llm.invoke(prompt)
    print(f"   Respuesta: {improved.content}\n")
    return {"response": improved.content, "iterations": iteration}


# ── Router: ¿seguir mejorando o terminar? ───────────────
def should_continue(state: State) -> str:
    if state["iterations"] < MAX_ITERATIONS:
        return "review"  # sigue el bucle
    return END  # sale del bucle


# ── Grafo con bucle ──────────────────────────────────────
#
#   START → generate → review ──┐
#                  ↑            │ (si iterations < MAX)
#                  └────────────┘
#                       │ (si iterations >= MAX)
#                      END
#
graph = StateGraph(State)
graph.add_node("generate", generate)
graph.add_node("review", review)

graph.add_edge(START, "generate")
graph.add_edge("generate", "review")
graph.add_conditional_edges(
    "review",
    should_continue,
    {
        "review": "review",  # vuelve a review (el bucle)
        END: END,  # termina
    },
)

app = graph.compile()

# ── Ejecución ────────────────────────────────────────────
print("Chatbot con auto-mejora en bucle. Escribe 'salir' para terminar.\n")
while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        break
    print()
    output = app.invoke({"text": user_input})
    print(f"✅ Respuesta final (tras {MAX_ITERATIONS} mejoras):")
    print(f"{output['response']}\n")
    print("-" * 50 + "\n")
