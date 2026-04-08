# historial list accumulates all user/assistant turns
# Passing the full historial on each invoke gives the agent conversation memory
# calcular_total checks stock before computing the total to avoid overselling

from deepagents import create_deep_agent
from langchain_ollama import ChatOllama

# ── Base de datos ─────────────────────────────────────────
productos = {
    "laptop": {"precio": 15000, "stock": 5},
    "mouse": {"precio": 350, "stock": 20},
    "teclado": {"precio": 800, "stock": 12},
    "monitor": {"precio": 6000, "stock": 3},
}


# ── Herramientas ──────────────────────────────────────────
def consultar_producto(nombre: str) -> str:
    """Consulta precio y stock de un producto en la tienda.

    Args:
        nombre: Nombre del producto a consultar (laptop, mouse, teclado, monitor)

    Returns:
        Precio y stock disponible del producto
    """
    nombre = nombre.lower()
    if nombre in productos:
        p = productos[nombre]
        return f"{nombre}: ${p['precio']} MXN | Stock: {p['stock']} unidades"
    return (
        f"Producto '{nombre}' no encontrado. Disponibles: {', '.join(productos.keys())}"
    )


def calcular_total(nombre: str, cantidad: int) -> str:
    """Calcula el costo total de comprar N unidades de un producto.

    Args:
        nombre: Nombre del producto (laptop, mouse, teclado, monitor)
        cantidad: Número de unidades a comprar

    Returns:
        El costo total de la compra o un mensaje de error si no hay stock
    """
    nombre = nombre.lower()
    if nombre not in productos:
        return f"Producto '{nombre}' no encontrado."
    p = productos[nombre]
    if cantidad > p["stock"]:
        return f"No hay suficiente stock. Solo hay {p['stock']} unidades disponibles."
    total = p["precio"] * cantidad
    return f"Total por {cantidad} {nombre}(s): ${total:,} MXN"


# ── System prompt ─────────────────────────────────────────
system_instructions = """Eres un asistente de ventas amable de TechStore, una tienda de tecnología en México. Sigue estas reglas:

1. Si el cliente pregunta por un producto: usa consultar_producto y responde con precio y stock de forma natural.
   Ejemplo: "La laptop cuesta $15,000 MXN y tenemos 5 unidades disponibles. ¿Te interesa?"

2. Si el cliente quiere saber el total de su compra: usa calcular_total y responde con el total de forma clara.
   Ejemplo: "Por 2 laptops el total sería $30,000 MXN."

3. Si no hay stock suficiente: informa amablemente y sugiere otra cantidad o producto.

4. Recuerda el contexto de la conversación para dar respuestas coherentes.

Siempre responde en español, de forma amable y directa. Nunca hagas preguntas innecesarias."""


# ── Modelo ────────────────────────────────────────────────
llm = ChatOllama(
    model="qwen3:14b",
    temperature=0,
    num_ctx=8192,
    extra_body={"think": False},
)

# ── Agente ────────────────────────────────────────────────
agent = create_deep_agent(
    model=llm,
    tools=[consultar_producto, calcular_total],
    system_prompt=system_instructions,
)

# ── Loop con memoria ──────────────────────────────────────
print("🛒 Bienvenido a TechStore. Escribe 'salir' para terminar.\n")
historial = []

while True:
    user_input = input("Cliente: ")
    if user_input.lower() == "salir":
        print("¡Hasta luego! Gracias por visitar TechStore. 👋")
        break

    historial.append({"role": "user", "content": user_input})

    result = agent.invoke({"messages": historial})
    respuesta = result["messages"][-1].content

    historial.append({"role": "assistant", "content": respuesta})
    print(f"Agente: {respuesta}\n")
