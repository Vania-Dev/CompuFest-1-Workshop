# 🤖 CompuFest[1] — AI Workshop El Umbral de los Autómatas Pensantes: Iniciación a los Laberintos de LangChain, LangGraph y DeepAgents

[![Contributors](https://img.shields.io/github/contributors/Vania-Dev/CompuFest-1-Workshop?style=for-the-badge&logo=github&label=Contributors&labelColor=101010)](https://github.com/Vania-Dev/CompuFest-1-Workshop/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/Vania-Dev/CompuFest-1-Workshop?style=for-the-badge&logo=github&label=Forks&labelColor=101010)](https://github.com/Vania-Dev/CompuFest-1-Workshop/forks)
[![Stars](https://img.shields.io/github/stars/Vania-Dev/CompuFest-1-Workshop?style=for-the-badge&logo=github&labelColor=101010)](https://github.com/Vania-Dev/CompuFest-1-Workshop/stargazers)
[![Issues](https://img.shields.io/github/issues/Vania-Dev/CompuFest-1-Workshop?style=for-the-badge&logo=github&label=Issues&labelColor=101010)](https://github.com/Vania-Dev/CompuFest-1-Workshop/issues)
[![License](https://img.shields.io/github/license/Vania-Dev/CompuFest-1-Workshop?style=for-the-badge&logo=open-source-initiative&labelColor=101010)](https://github.com/Vania-Dev/CompuFest-1-Workshop/blob/main/LICENSE.txt)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Vania-Dev">
    <img src="images/vaniadev.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">El Umbral de los Autómatas Pensantes: Iniciación a los Laberintos de LangChain, LangGraph y DeepAgents</h3>

  <a href="https://www.youtube.com/playlist?list=PLZLvS5NXZVysi0nnN6B3XpSw_6q-0ur5x">
    <img src="images/video.jpg" alt="Logo" style="height: 60%; width:60%;">
  </a>

  <p align="center">
    <br />
    <a href="https://github.com/Vania-Dev/CompuFest-1-Workshop">Aditional material</a>
    ·
    <a href="https://github.com/Vania-Dev/CompuFest-1-Workshop/issues/new?labels=bug&template=bug-report---.md">Report an Error</a>
    ·
    <a href="https://github.com/Vania-Dev/CompuFest-1-Workshop/issues/new?labels=enhancement&template=feature-request---.md">Request an Upgrade</a>
  </p>
</div>

## ✨ About Project

Hands-on workshop presented at **CompuFest[1]**, designed to introduce developers to building AI-powered applications using **LangChain**, **LangGraph**, and **DeepAgents** with local LLMs via Ollama.

Each folder is a self-contained learning module that progressively builds on the previous one — from simple prompt templates to autonomous agents with memory.

---

## 📁 Project Structure

```
CompuFest-1-Workshop/
├── LangChain/
│   ├── 01_PromptTemplate.py     # Basic prompt formatting with PromptTemplate
│   ├── 02_Chain.py              # Building a simple LLM chain with LCEL
│   └── 03_SequentialChain.py   # Multi-step sequential chain
├── LangGraph/
│   ├── 01_SimpleNode.py         # Single-node state graph
│   ├── 02_LogicRouter.py        # Conditional routing between nodes
│   └── 03_LoopGraph.py          # Self-improving loop graph
├── DeepAgents/
│   ├── 01_HelloWorld.py         # Agent with two basic tools
│   ├── 02_MultipleTools.py      # Agent with multiple utility tools
│   └── 03_AgentMemory.py        # Agent with conversation memory
├── main.py
├── requirements.txt
└── pyproject.toml
```

---

## 📦 Modules

### 🔗 LangChain — Prompt & Chain Fundamentals

Covers the core building blocks of LangChain: prompt templates, model invocation, and chaining steps together using LCEL (LangChain Expression Language).



### 🕸️ LangGraph — Stateful Graph Workflows

Introduces stateful, graph-based workflows where nodes process a shared state and edges define the execution flow — including conditional routing and loops.

### 🤖 DeepAgents — Tool-Using Autonomous Agents

Builds agents that can reason, select tools, and maintain conversation history across turns using `create_deep_agent` from the `deepagents` library.


## 🔄 Flow Diagrams

### LangChain — Prompt Template (`01_PromptTemplate.py`)

```mermaid
flowchart LR
    A[Input Text] --> B[PromptTemplate]
    B --> C[LLM]
    C --> D[Summary + Key Idea]
```

---

### LangChain — Chain (`02_Chain.py`)

```mermaid
flowchart LR
    A[Question] --> B[ChatPromptTemplate]
    B --> C[LLM]
    C --> D[Response]
```

---

### LangChain — Sequential Chain (`03_SequentialChain.py`)

```mermaid
flowchart LR
    A[User Input] --> B[Analyze Intent]
    B --> C[Generate Response]
    C --> D[Final Response]
```

---

### LangGraph — Simple Node (`01_SimpleNode.py`)

```mermaid
flowchart LR
    A[Input Text] --> B[Generate Node]
    B --> C[Response]
```

---

### LangGraph — Logic Router (`02_LogicRouter.py`)

```mermaid
flowchart TD
    A[User Input] --> B{Router}
    B -->|short input| C[Clarify]
    B -->|enough words| D[Generate]
    C --> E[END]
    D --> E
```

---

### LangGraph — Loop Graph (`03_LoopGraph.py`)

```mermaid
flowchart TD
    A[User Input] --> B[Generate]
    B --> C[Review]
    C -->|iterations < MAX| C
    C -->|iterations >= MAX| D[END]
```

---

### DeepAgents — Hello World (`01_HelloWorld.py`)

```mermaid
flowchart LR
    A[Question] --> B[Agent]
    B -->|math| C[calculator]
    B -->|weather| D[get_weather]
    C --> E[Answer]
    D --> E
```

---

### DeepAgents — Multiple Tools (`02_MultipleTools.py`)

```mermaid
flowchart LR
    A[User Input] --> B[Agent]
    B -->|time| C[obtener_hora]
    B -->|temperature| D[convertir_temperatura]
    B -->|text| E[contar_palabras]
    C --> F[Response]
    D --> F
    E --> F
```

---

### DeepAgents — Agent with Memory (`03_AgentMemory.py`)

```mermaid
flowchart TD
    A[User Message] --> B[Agent + History]
    B --> C{Use Tool?}
    C -->|yes| D[Run Tool]
    C -->|no| E[Direct Answer]
    D --> E
    E -->|next turn| A
```

---

## ⚙️ Requirements

```
langchain==1.2.15
langchain-classic>=1.0.0
langchain-community==0.4
langchain-core==1.2.27
langchain-ollama==1.0.1
langgraph>=1.1.6
deepagents>=0.5.1
```

> **Python >= 3.11** required.  
> All examples use **Ollama** as the local LLM backend. Make sure Ollama is running and the required models are pulled before executing any script.

### Install

```bash
# Using pip
pip install -r requirements.txt

# Using uv (recommended)
uv sync
```

### Pull required models

```bash
ollama pull gpt-oss:20b   # used in LangChain and LangGraph examples
ollama pull qwen3:14b     # used in DeepAgents examples
```

---

## 🚀 Running Examples

```bash
# LangChain
uv run LangChain/01_PromptTemplate.py
uv run LangChain/02_Chain.py
uv run LangChain/03_SequentialChain.py

# LangGraph
uv run LangGraph/01_SimpleNode.py
uv run LangGraph/02_LogicRouter.py
uv run LangGraph/03_LoopGraph.py

# DeepAgents
uv run DeepAgents/01_HelloWorld.py
uv run DeepAgents/02_MultipleTools.py
uv run DeepAgents/03_AgentMemory.py
```

---

## 🧠 Learning Path

```
LangChain/01  →  LangChain/02  →  LangChain/03
     ↓
LangGraph/01  →  LangGraph/02  →  LangGraph/03
     ↓
DeepAgents/01 →  DeepAgents/02 →  DeepAgents/03
```

Each step introduces one new concept on top of the previous, making this workshop suitable for developers new to LLM application development.

<!-- LICENSE -->
## 📄 License

Distributed under the MIT license. See the `LICENSE.txt` file for more information.


<!-- CONTACT -->
## 📧 Contacto

[![YouTube](https://img.shields.io/badge/YouTube-vaniadev-FF0000?style=for-the-badge&logo=youtube&logoColor=white&labelColor=101010)](https://youtube.com/@VANIADEV)
[![Instagram](https://img.shields.io/badge/Instagram-@vania_dev_-E4405F?style=for-the-badge&logo=instagram&logoColor=white&labelColor=101010)](https://www.instagram.com/vania_dev_/)
[![TikTok](https://img.shields.io/badge/TikTok-@vania_dev_-69C9D0?style=for-the-badge&logo=tiktok&logoColor=white&labelColor=101010)](https://www.tiktok.com/@vania_dev_)
[![Facebook](https://img.shields.io/badge/Facebook-@vaniadev-1877F2?style=for-the-badge&logo=facebook&logoColor=white&labelColor=101010)](https://www.facebook.com/SMAEMX)
[![Link](https://img.shields.io/badge/Links-vaniadev-39E09B?style=for-the-badge&logo=Linktree&logoColor=white&labelColor=101010)](https://beacons.ai/vaniadev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ivan_Castañeda-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/ivan-castaneda-nazario/)
[![Web](https://img.shields.io/badge/Web-vaniadev-14a1f0?style=for-the-badge&logo=dev.to&logoColor=white&labelColor=101010)](https://vaniadev.super.site/)
[![BuyMeACoffee](https://img.shields.io/badge/Buy_Me_A_Coffee-apoya_mi_trabajo-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white&labelColor=101010)](https://buymeacoffee.com/vania_vaniusha)

---

<div align="center">

**Hazlo con el tipo de ❤️ que deja huellas en el alma**

[⭐ Star this repo](https://github.com/Vania-Dev/CompuFest-1-Workshop) • [🐛 Report Bug](https://github.com/Vania-Dev/CompuFest-1-Workshop/issues) • [✨ Request Feature](https://github.com/Vania-Dev/CompuFest-1-Workshop/issues)

</div>