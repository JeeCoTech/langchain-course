from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily_client = TavilyClient()


@tool
def search(query:str) -> str:
    """
    Tool that searches over internet
    Args:
        query: TThe query to search for
    Returns:
        The search results
    """
    print(f"search for {query}")
    return tavily_client.search(query=query, num_results=3, timeout=5)

llm = ChatOpenAI(model="gpt-5")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})
    print(result)
if __name__ == "__main__":
    main()