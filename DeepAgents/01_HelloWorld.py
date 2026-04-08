# calculator() uses eval() to compute math expressions
# get_weather() returns a mocked weather string for a given city
# extra_body={"think": False} disables Qwen3's internal chain-of-thought

from deepagents import create_deep_agent
from langchain_ollama import ChatOllama


def calculator(expression: str) -> str:
    """Calculate a mathematical expression. Use this for any math operations like multiplication, addition, subtraction, division.
    
    Args:
        expression: A mathematical expression to evaluate (e.g., "25 * 4", "10 + 5")
    
    Returns:
        The result of the calculation
    """
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"


def get_weather(location: str) -> str:
    """Get the current weather for a location.
    
    Args:
        location: City name
    
    Returns:
        Current weather conditions
    """
    return f"Weather in {location}: Sunny, 22°C"


system_instructions = """You are a concise assistant. Follow these rules strictly:

1. When asked a math question: use the calculator tool, then reply ONLY with:
   "The result of [expression] is [result]."

2. When asked about weather: use the get_weather tool, then reply ONLY with:
   "The weather in [city] is [conditions]."

Never ask follow-up questions. Never add extra commentary. Just answer directly."""

model_name = "qwen3:14b"

llm = ChatOllama(
    model=model_name,
    temperature=0,
    num_ctx=8192,          # ← sube el contexto para evitar el tope de 4096
    extra_body={"think": False},  # ← desactiva el thinking mode
)

agent = create_deep_agent(
    model=llm, tools=[calculator, get_weather], system_prompt=system_instructions
)

# ── Helper ────────────────────────────────────────────────
def ask(question: str):
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    print(f"Q: {question}")
    print(f"A: {result['messages'][-1].content}")
    print("--------")

ask("What is 25 * 4 * 10?")
ask("What is the temperature at Mexico City?")