# Three tools: obtener_hora, convertir_temperatura, contar_palabras
# Each tool has a docstring — DeepAgents uses it to decide when to call it
# Interactive loop lets the user test all tools in a single session

from datetime import datetime

from deepagents import create_deep_agent
from langchain_ollama import ChatOllama


# ── Herramientas ─────────────────────────────────────────
def obtener_hora() -> str:
    """Devuelve la fecha y hora actual."""
    return datetime.now().strftime("Hoy es %A %d de %B de %Y, son las %H:%M")


def convertir_temperatura(celsius: float) -> str:
    """Convierte grados Celsius a Fahrenheit y Kelvin.

    Args:
        celsius: Temperatura en grados Celsius a convertir

    Returns:
        La temperatura convertida a Fahrenheit y Kelvin
    """
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    return f"{celsius}°C = {fahrenheit:.1f}°F = {kelvin:.2f}K"


def contar_palabras(texto: str) -> str:
    """Cuenta las palabras y caracteres de un texto.

    Args:
        texto: El texto a analizar

    Returns:
        El número de palabras y caracteres del texto
    """
    palabras = len(texto.split())
    caracteres = len(texto)
    return f"El texto tiene {palabras} palabras y {caracteres} caracteres."


# ── System prompt ─────────────────────────────────────────
system_instructions = """Eres un asistente conciso y directo. Sigue estas reglas estrictamente:

1. Si te preguntan la hora o fecha: usa obtener_hora y responde SOLO con:
   "Son las [hora] del [fecha]."

2. Si te piden convertir temperatura: usa convertir_temperatura y responde SOLO con:
   "[celsius]°C equivale a [fahrenheit]°F y [kelvin]K."

3. Si te piden contar palabras o caracteres: usa contar_palabras y responde SOLO con:
   "El texto tiene [N] palabras y [N] caracteres."

Nunca hagas preguntas adicionales. Nunca agregues comentarios extra. Responde directo."""


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
    tools=[obtener_hora, convertir_temperatura, contar_palabras],
    system_prompt=system_instructions,
)

# ── Loop interactivo ──────────────────────────────────────
print("Agente listo. Escribe 'salir' para terminar.\n")
while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        break
    result = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
    print(f"Agente: {result['messages'][-1].content}\n")
