# Generative AI – LangChain Overview

## 1. Fundamentals

### **LangChain**

**Definition:** A framework designed to build applications powered by LLMs.
**What it does:** Provides standardized building blocks (models, prompts, memory, chains, agents) that simplify LLM app development.

### **LangChain Components**

**Definition:** The modular parts of LangChain that interact to build pipelines.
**What it does:** Lets you plug together prompts, models, tools, memory, retrievers, and chains to create end-to-end workflows.

### **Models**

**Definition:** LLM interfaces (chat models, text models, embedding models) in LangChain.
**What it does:** Handles text generation, embeddings, reasoning, and tool interactions through unified wrappers.

### **Prompts**

**Definition:** Instructions/templates given to the model.
**What they do:** Shape the model’s behavior, structure expected tasks, and ensure predictable outputs.

### **Parsing Outputs**

**Definition:** Methods to structure, validate, and interpret model responses.
**What it does:** Converts raw LLM text into JSON, Pydantic objects, lists, or other deterministic formats.

### **Runnables & LCEL**

**Definition:** The executable interface (Runnable) and the LangChain Expression Language (LCEL).
**What it does:** Lets you connect components like Lego blocks — prompts → model → parser — using a clean, functional syntax.

### **Chain**

**Definition:** A sequence of steps connected into a pipeline.
**What it does:** Automates multi-step tasks such as retrieval + generation, prompting + parsing, or reasoning + action.

### **Memory** *(yet to study)*

**Definition:** A mechanism to store context across interactions.
**What it does:** Enables chat-like behavior, entity tracking, and stateful agents.

---

## 2. RAG (Retrieval-Augmented Generation)

### **Document Loaders**

**Definition:** Interfaces that load external data from files, URLs, databases, etc.
**What it does:** Brings raw knowledge into your RAG pipeline.

### **Text Splitters**

**Definition:** Utilities that break long text into manageable chunks.
**What they do:** Improve embedding relevance and retrieval accuracy by producing optimal-sized segments.

### **Embedding**

**Definition:** Vector representation of text generated using embedding models.
**What it does:** Converts text into numeric vectors for similarity search.

### **Vector Stores**

**Definition:** Databases optimized for storing and querying embeddings.
**What they do:** Support fast nearest-neighbor search to fetch relevant chunks.

### **Retrievers**

**Definition:** Components that fetch the most relevant document chunks for a query.
**What they do:** Form the “retrieval” part of RAG before sending context to the LLM.

### **Building a RAG Application**

**Definition:** The complete architecture combining loaders, splitters, embeddings, vector stores, retrievers, and LLMs.
**What it does:** Creates knowledge-aware systems capable of answering queries using external documents.

---

## 3. Agents

### **Tools and Toolkit**

**Definition:** Functions and APIs that the agent is allowed to call.
**What it does:** Gives the model real-world abilities like searching, database access, code execution, or arithmetic.

### **Tool Calling**

**Definition:** The structured protocol where an LLM decides whether it should call a tool, and then provides arguments for it.
**What it does:** Enables LLMs to execute tools logically instead of hallucinating answers.

### **Building an AI Agent**

**Definition:** Creating a system that can reason, plan, choose tools, retrieve data, and act autonomously.
**What it does:** Produces actionable, workflow-capable agents (planners, assistants, automation systems).

---

# Reference Links

### **LangChain Fundamentals**

* LangChain Concepts: [https://python.langchain.com/docs/concepts/](https://python.langchain.com/docs/concepts/)
* Components Overview: [https://www.deepchecks.com/langchain-components-a-comprehensive-beginners-guide/](https://www.deepchecks.com/langchain-components-a-comprehensive-beginners-guide/)
* Models Overview: [https://docs.langchain.com/oss/python/langchain/overview](https://docs.langchain.com/oss/python/langchain/overview)
* Memory Docs: [https://docs.langchain.com/oss/python/memory](https://docs.langchain.com/oss/python/memory)

### **RAG**

* RAG Concepts (overall): [https://python.langchain.com/docs/concepts/](https://python.langchain.com/docs/concepts/)
* VectorStores Guide: [https://python.langchain.com/docs/integrations/vectorstores/](https://python.langchain.com/docs/integrations/vectorstores/)
* Embeddings: [https://python.langchain.com/docs/integrations/text_embedding/](https://python.langchain.com/docs/integrations/text_embedding/)

### **Agents**

* LangChain Tools: [https://docs.langchain.com/oss/python/langchain/tools](https://docs.langchain.com/oss/python/langchain/tools)
* Agent Tool Calling: [https://python.langchain.com/v0.1/docs/modules/agents/agent_types/tool_calling/](https://python.langchain.com/v0.1/docs/modules/agents/agent_types/tool_calling/)
* Build an Agent (IBM tutorial): [https://www.ibm.com/think/tutorials/using-langchain-tools-to-build-an-ai-agent](https://www.ibm.com/think/tutorials/using-langchain-tools-to-build-an-ai-agent)

---

If you want, I can format this into a **full README**, add **code examples**, or convert this into **Notion-friendly blocks**.
