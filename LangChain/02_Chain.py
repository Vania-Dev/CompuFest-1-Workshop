# Creates a ChatPromptTemplate with system + human messages
# Uses LCEL pipe (|) to connect template → model into a chain
# streaming=True would allow real-time token output

# Importamos ChatOllama para interactuar con modelos de Ollama
# Importamos ChatPromptTemplate para crear plantillas de conversación
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# BLOQUES DE CONSTRUCCIÓN (Building Blocks)
# Creamos una plantilla de chat simple con un mensaje de sistema y uno humano
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{question}"),
    ]
)

# Definimos el modelo que vamos a usar
model_name = "gpt-oss:20b"
# Creamos una instancia del modelo ChatOllama
# streaming=True permite que las respuesta se genere y se imprima en tiempo real.
model = ChatOllama(model=model_name, temperature=0)

chain = template | model

response = chain.invoke({"question": "Which model providers offer LLMs?"})

print(response.content)
