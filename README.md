# LangChain Course — Layer 1: Agent Loop (Tool Calling)

This README provides a short, clear, step-by-step setup and a focused guide for the "Layer 1: Agent Loop using LangChain tool calling" demo.

## Prerequisites
1. Windows machine, PowerShell or CMD.
2. Python 3.10+ installed.
3. Ollama installed and running (for local models).
4. An OpenAI API key (if using OpenAI) and a LangSmith key (for tracing) if you want LangSmith traces.
5. Recommended formatting tools: black, isort (optional).

## Setup (recommended)
1. Open PowerShell in the repo folder:
   - cd c:\Technical\Github-Tech\langchain-course
2. Create and activate a virtual environment:
   - python -m venv .venv
   - .venv\Scripts\Activate.ps1
3. Install dependencies:
   - pip install langchain langchain-ollama langchain-openai python-dotenv black isort
   - Or add packages using your preferred package manager (uv) if you use one:
     - uv install
     - uv add langchain langchain-ollama langchain-openai python-dotenv black isort
4. Create a `.env` file in the repo root with:
   - OPENAI_API_KEY=your_openai_key
   - LANGSMITH_API_KEY=your_langsmith_key
   - (Add any other keys required for your model provider.)

## Ollama (local model) quick steps
1. Pull or run a Qwen model with Ollama:
   - ollama pull qwen-7b
   - ollama run qwen-7b
2. To serve as a local model endpoint:
   - ollama serve
3. Confirm Ollama is running before starting the agent.

## Layer 1: Agent Loop — Tool Calling (high level)
Goal: Demonstrate LangChain tool-calling with an agent loop that:
- Exposes simple tools (Python functions) decorated with @tool.
- Uses a chat model (local via Ollama or remote) with init_chat_model.
- Iteratively calls tools and passes results back to the model until a final answer or MAX_ITERATIONS.

## Layer 1: Implementation Steps (concise)
1. Define constants:
   - MAX_ITERATIONS (e.g., 10)
   - MODEL identifier (e.g., "qwen-7b" or your Ollama model string)
2. Import required modules:
   - langchain init_chat_model, SystemMessage, HumanMessage, Tool decorator (or relevant helper)
   - traceable decorator from langsmith (if tracing)
   - dotenv to load .env
3. Implement tools (example signatures):
   - @tool
     def get_product_price(product_name: str) -> float:
       - return price (mock or lookup)
   - @tool
     def apply_discount(price: float, tier: str) -> float:
       - calculate and return discounted price
4. Build tool collection and a dictionary mapping tool names to callables (LangChain expects this).
5. Initialize the chat model:
   - model = init_chat_model(MODEL, temperature=0.0)
   - bind or attach tools to the model/agent as your LangChain version requires.
6. Compose messages:
   - SystemMessage: agent behavior, constraints, and tool usage guidance.
   - HumanMessage: the user question or task.
7. Agent loop:
   - For up to MAX_ITERATIONS:
     - Send current messages to the model.
     - If the model responds with a tool call, run the corresponding tool, collect output.
     - Append tool output to messages and continue.
     - If model returns a final answer (no tool call), break and return the answer.
8. (Optional) Use @traceable on run_agent to enable LangSmith tracing.

## Minimal pseudocode outline
```python
# filepath: c:\Technical\Github-Tech\langchain-course\agent_example.py
# ...existing code...
from langchain import init_chat_model, SystemMessage, HumanMessage
from langchain.tools import tool
from langsmith import traceable
from dotenv import load_dotenv
load_dotenv()

MAX_ITERATIONS = 10
MODEL = "qwen-7b"

@tool
def get_product_price(name: str) -> float:
    return 9.99  # replace with real lookup

@tool
def apply_discount(price: float, tier: str) -> float:
    discounts = {"gold": 0.2, "silver": 0.1}
    return price * (1 - discounts.get(tier, 0.0))

@traceable
def run_agent(user_question: str) -> str:
    model = init_chat_model(MODEL, temperature=0.0)
    tools = {"get_product_price": get_product_price, "apply_discount": apply_discount}
    messages = [SystemMessage(content="You are a helpful agent that may call tools."),
                HumanMessage(content=user_question)]
    for _ in range(MAX_ITERATIONS):
        response = model.generate(messages)  # adjust to your LangChain API version
        if response.calls_tool:
            result = tools[response.tool_name](*response.tool_args)
            messages.append(HumanMessage(content=f"Tool result: {result}"))
            continue
        return response.text
    return "Max iterations reached"
# ...existing code...
```

## Tips & Troubleshooting
- Use temperature=0.0 for deterministic tool-routing behavior.
- Validate tool inputs/outputs to avoid malformed messages.
- If Ollama model names differ, replace MODEL string accordingly.
- Enable LangSmith tracing only after confirming basic agent behavior.

## Licensing / Notes
- Keep model binary downloads and usage in accordance with the model license.
- Adjust example code to match your installed LangChain version (APIs evolve).

## Layer 1: Agent Loop — Raw function Calling
This example shows how to build a manual tool-calling agent loop with Ollama and LangSmith, without using LangChain’s @tool decorator or agent abstractions.

The script includes:

ollama for model interaction
traceable from langsmith for tracing LLM calls and tool execution
two tool functions: get_product_price and apply_discount
manual JSON schema definitions for tool calling

#### Key Concepts ####
Import only ollama
Import traceable from langsmith
Use Ollama function calling without @tool
Define tool metadata and arguments manually using JSON schema
Trace both tool execution and LLM calls with LangSmith
Functions
The same functions used in this example are:

```python 
get_product_price(product: str) -> float
```
Looks up the product price in a catalog
```python
apply_discount(price: float, discount_tier: str) -> float
```
Applies a discount tier to the price and returns the final price
Manual Tool Schema
Because @tool is not used, the tool definitions are written manually as JSON schema objects.

Each tool entry includes:

name
description
parameters
required fields
This is how Ollama knows the tool signature and arguments.

Message Format
The message format is built manually using plain dictionaries:

{"role": "system", "content": ...}
{"role": "user", "content": ...}
{"role": "tool", "content": ...}
This differs from LangChain’s higher-level message classes such as:

SystemMessage
HumanMessage
AIMessage
Agent Loop Behavior

The agent loop:
Sends messages to ollama.chat
Checks if the model returned a tool call
Executes the first tool call manually
Appends the tool result as a tool message
Repeats until the model returns a final answer
Differences Listed in the File
Difference 1: We don’t use @tool decorator.
Difference 2: Without @tool, we must MANUALLY define the JSON schema for each function.
Difference 3: Without LangChain, we must manually trace LLM calls for LangSmith.
Difference 4: Format of messages is different from LangChain’s SystemMessage/HumanMessage/AIMessage classes.
Difference 5: ollama.chat() directly instead of llm_with_tools.invoke().
Difference 6: Attribute access (.function.name) instead of dict access (.get("name")).
Difference 7: Direct function call instead of tool.invoke().
Why This Approach
This example demonstrates the lower-level mechanics of tool calling:

manual tool registration
explicit message management
direct function execution
explicit tracing

### Layer 2 : ReAct prompt ###
In thie section we will use the React Prompt for tool calling instead of Langchain or Ollama

We need to use he regualr exprssion as we use the prompt for tool calling
We need to use the tool dictionary (tools) which contains the tool name

Since we use the prompt, we need to use the inspect to get the signature and docstring. This is then later propagated to LLM. 

We then get the tool description based on the tools and then we get tool names 

IN the react prompt we then need to configure the tool description and then tool names to the ReAct prompt. 

In ollama_chat_traced fucntion, we are using the model, messges and options which will call the ollama chat model. 

We are not using any message prompt instead we are using the ReAct Prompt. 
Scrathpad containts the action taken by the LLM so far
When we iterate the iteration we send the full prompt as a combination of prompt and details of the scrath pad. 

Once the LLM generates the LLM output after the LLM execution , we can use thettribute as "Final Answer"