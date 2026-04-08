# Two-step chain: intent analysis → response generation
# StrOutputParser converts AIMessage to plain string between steps
# Lambda bridges the two prompts by reshaping the intermediate output

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# Model setup
model_name = "gpt-oss:20b"
model = ChatOllama(model=model_name, temperature=0)

# Step 1: Analysis prompt
analysis_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert at analyzing user intent."),
        ("human", "Analyze the intent of the following text:\n{input}"),
    ]
)

# Step 2: Response prompt
response_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate a helpful response based on this analysis:\n{analysis}"),
    ]
)

# Parser to extract string content between chains
parser = StrOutputParser()

# Sequential chain using LCEL pipe syntax
# The output of each step feeds into the next
chain = (
    analysis_prompt
    | model
    | parser
    | (lambda analysis: {"analysis": analysis})
    | response_prompt
    | model
    | parser
)

result = chain.invoke({"input": "I want to learn LangGraph"})
print(result)
