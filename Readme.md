### Pre-installation

1. Create a Python virtual environment.
2. Install dependencies:
   - `langchain`
   - `langchain-openai`
   - `langgraph`
   - `tavily`
   - `python-dotenv`
   - `black`
   - `isort`

3. Create a `.gitignore` file.
4. Create a `.env` file with these variables:
   - `LANGSMITH_TRACING=`
   - `LANGSMITH_ENDPOINT=`
   - `LANGSMITH_API_KEY=`
   - `LANGSMITH_PROJECT=`
   - `TAVILY_API_KEY=`
   - `OPENAI_API_KEY=`

### Project overview

This repository implements a LangGraph-based reasoning flow using a chat LLM and external tools. The main logic is split across three files:

1. `react.py`
2. `nodes.py`
3. `main.py`

### `react.py`

- Imports:
  - `Tools`
  - `ChatOpenAI`
  - `TavilySearch`
- Defines a helper function `triple` and marks it with a tool decorator.
- Configures function calling and reasoning.
- Creates a ChatLLM instance using `ChatOpenAI` with:
  - model selection
  - temperature
  - bound tools

This file is responsible for connecting the language model to the external tool set and exposing the tool interface for reasoning.

### `nodes.py`

- Imports:
  - `MessageState`
  - `ToolNode`
- Defines the agent reasoning node `run_agent_reasoning(message_state)`.
- Inside the node:
  - calls `llm.invoke(...)`
  - passes the system message and the current message state
  - returns the response
- Builds a `ToolNode` object that wraps the available tools.

This file encapsulates agent reasoning and tool integration as LangGraph nodes.

### `main.py`

- Imports:
  - `HumanMessage`
  - `MessageState`
  - `StateGraph`
- Defines the node names / states:
  - `Agent_Reason`
  - `ACT`
  - `LAST`
- Builds the control flow:
  - creates a `StateGraph` with `MessageState`
  - adds the reasoning node `run_agent_reasoning`
  - adds the `ACT` tool node
  - configures conditional branching:
    - if the current message indicates it is the last step, end the flow
    - otherwise continue with `ACT`
  - adds an edge from `ACT` back to `Agent_Reason`
- Compiles the graph and generates a Mermaid PNG file
- Invokes the app with a human message
- Prints the final message content

### How to run

1. Ensure `.env` is populated.
2. Run the main script:
   - `python main.py`
3. Check the generated Mermaid graph output and the printed final message.

### Notes

- `react.py` handles model/tool setup.
- `nodes.py` handles LangGraph node definitions.
- `main.py` builds the graph, compiles it, and executes the agent reasoning flow.

Flow Diagrams

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)