from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

tavily = TavilyClient()
load_dotenv()

@tool
def search(query: str) -> str:
    """
        Tool that searches the internet
        Args:
            query: The query to search for
        Returns:
            The Search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatGroq(temperature=0, model="openai/gpt-oss-120b")
tools=[search]
agent=create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-ai-job-search-agent!")
    result=agent.invoke({
        "messages": HumanMessage(content="Search for 3 job postings for an ai engineer using langchain in cairo on linkedin and list their details")
        })
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
