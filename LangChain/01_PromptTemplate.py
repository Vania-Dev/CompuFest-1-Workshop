# Defines a PromptTemplate with a single {text} variable
# Formats the prompt and sends it directly to the LLM
# Returns a one-sentence summary and one key idea

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# Definimos el modelo que vamos a usar
model_name = "gpt-oss:20b"

# Initialize Ollama LLM
llm = ChatOllama(model=model_name, temperature=0)

# Define a structured prompt
prompt = PromptTemplate(
    input_variables=["text"],
    template="""
        Analyze the following text and return:
        - One sentence summary
        - One key idea

        Text:
        {text}
""",
)

formatted_prompt = prompt.format(
    text="LangChain helps developers build applications with LLMs."
)

response = llm.invoke(formatted_prompt)
print(response.content)
