# LangChain Course Notes

## Section 1: What Are Agents?

Agents are systems that make decisions and take actions based on the response from an LLM instead of following a fixed, predefined flow.

Typical workflow:
1. The user sends a query.
2. The LLM reasons about the request.
3. The agent decides whether an action is needed.
4. If needed, the agent calls a tool.
5. The tool returns observations.
6. The LLM uses those observations to continue reasoning.
7. The process repeats until the agent can provide a final answer.

Flow:
Query -> LLM reasoning -> Action -> Tool -> Observations -> LLM -> Final answer

## Section 2: Evolution of Agent Approaches

The main evolution of agent design in LangChain is:

ReAct Agent -> Tool Calling Agent -> LangGraph ReAct Agent -> LangChain create_agent() (v1.0)

Summary:
- ReAct Agent: uses a reasoning-and-action prompt style.
- Tool Calling Agent: uses function/tool calling.
- LangGraph ReAct Agent: uses a graph-based workflow.
- create_agent(): the newer and simpler way to build agents in LangChain.

## Section 3: Using create_agent() in LangChain

Follow these steps to build a simple agent.

### Step 1: Initialize the project
Create a Python project and a virtual environment.

```bash
uv init
uv venv
```

### Step 2: Add packages
Add the necessary packages:

- LangChain
- Pythondotenv
- langchain
- langchain-openai
- langchain-tavily (tavily is integrated with LangChain)
- tavily-python (original Tavily SDK)

### Step 3: Add a boilerplate code
Add a simple Python file to start the agent.

### Step 4: Set up environment variables
Set the following environment variables:

- `LANGSMITH_TRACING`
- `LANGSMITH_ENDPOINT`
- `LANGSMITH_API_KEY`
- `LANGSMITH_PROJECT`
- `TAVILY_API_KEY`
- `OPENAI_API_KEY`

### Step 5: Import the create_agent function
Import the `create_agent` function from `langchain.agents`.

### Step 6: Import tools and messages
Import tools from `langchain.tools` and messages from `langchain.messages` and `ChatOpenAI` from `langchain_openai`.

### Step 7: Define tools
Tools are functions that can be used by the LLM to execute when needed.

### Step 8: Implement a search agent
Implement a search agent that will search the internet and get the response.

### Step 9: Convert a regular Python function to a LangChain tool
Convert a regular Python function to a LangChain tool by adding the `@tool` decorator.

### Step 10: Create an agent
Create an agent by instantiating the `ChatOpenAI()`.

### Step 11: Define the tool as a search tool
Define the tool as a search tool.

### Step 12: Create an agent using create_agent
Create an agent using `create_agent` by passing the model and tools.

### Step 13: Run the agent
Run the agent using `agent.invoke` by passing the message (like a Human Message) and get the result.

### Step 14: When we create an agent
When we create an agent, we send the list of tools to the LLM and not the agent.

### Step 15: Trace the invocation
We can trace the invocation using the LangSmith.

### Step 16: The sequence of events
The sequence of events is:

- Human message is sent to agent
- Agent creates an AI message
- Then Tool message is created
- AI agent (LLM) will sent the final result

### Using the LangChain Tavily

Import the Tavily client from the `tavily` package and initialize it as follows:
```python
langchain_tavily import tavily search
```

use the tavily search directly as a tool . By doing this we can remove the use of defining the tool and use the tavily search of the langcahin itself

If you want, I can also make it sound more formal, more beginner-friendly, or more concise.

### Pydantic Object

Pydantic is used to define and validate the format of the agent's response. We import `BaseModel` and `Field` from `pydantic`.

We create a `Source` class by extending `BaseModel` and define a string field with a description using `Field`. We also define an `AgentResponse` class to describe the overall structure of the agent's output, including the response content and its source.

Once the response schema is defined, we pass it to the agent function so the generated output follows the expected structure.


Langchain structured output help to give output in the structured format. Using the strcutured output we have 2 approaches 
Toolstratergy and Providerstratergy. ProviderStartergy is used by default. 

