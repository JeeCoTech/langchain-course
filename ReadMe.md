# Reflexion Agent — Project README

## Overview
This repository implements a Reflexion-style agent using LangChain and LangGraph. It includes:
- chain.py: agent prompts and chains
- tool_executor.py: external tool wrappers (e.g., Tavily)
- schemas.py: Pydantic schemas for agent I/O
- main.py: graph orchestration that wires chains and tools

## Project setup (Windows)
1. Create and activate a virtual environment:
   - PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - CMD:
     ```cmd
     python -m venv .venv
     .\.venv\Scripts\activate.bat
     ```

2. Install dependencies:
   ```powershell
   pip install --upgrade pip
   pip install langchain langchain-openai langgraph tavily langsmith-client black isort python-dotenv
   ```

3. Create a `.env` file in the repository root and set required environment variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   LANGSMITH_API_KEY=your_langsmith_api_key
   LANGSMITH_ENDPOINT=https://api.langsmith.example
   LANGSMITH_PROJECT=your_project_name
   LANGSMITH_TRACING=true
   TAVILY_API_KEY=your_tavily_api_key
   ```

4. Run the application:
   ```powershell
   python main.py
   ```

## Files and responsibilities
- main.py
  - Entry point that builds a LangGraph (StateGraph), adds nodes for draft/revise/tool execution, and runs the event loop.
  - Orchestrates iterations, tool call counts, and termination conditions.

- chain.py
  - Loads environment variables (dotenv).
  - Defines prompts (actor/first responder/revisor) and prompt templates.
  - Declares the ChatOpenAI LLM bindings (model name, temperature).
  - Uses structured output parsers (JsonOutputToolsParser or PydanticToolParser) consistent with schemas.py.
  - Creates responder and revisor chains and exposes invocation methods.

- schemas.py
  - Pydantic models that describe structured inputs/outputs:
    - Reflection
    - AnswerQuestion
    - ReviseAnswer

- tool_executor.py
  - Wraps external tools (TavilySearch) into LangChain StructuredTool/ToolNode.
  - Implements run_queries() to batch-search and return structured results.
  - Exposes execute_tools for use in the graph.

## Creating the LangGraph (main.py)
- Import necessary packages from LangChain and LangGraph.
- Import chain and executor components.
- Define nodes:
  - Draft node (first responder) that returns the initial message.
  - Revise node that takes the message state, invokes the revisor, and returns the revised response.
  - Tool execution node that runs external queries and returns results.
- Implement an event loop that:
  - Tracks tool call counts and iterations.
  - Stops when termination conditions are met.

## Development notes / TODOs
- Ensure chain.py uses parsers consistent with schemas.py (JsonOutputToolsParser vs PydanticToolParser).
- Confirm the LLM model name and LangSmith integration in chain.py.
- Add unit tests for tool_executor.run_queries and schema validation.
- Format code with `black` and `isort`.

## Diagram
Reflexion Agent architecture image (replace `image.png` with the actual diagram as needed).
![alt text](image.png)