from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

load_dotenv()


llm = ChatGroq(temperature=0, model="llama-3.3-70b-versatile")
tools=[TavilySearch()]
agent=create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-ai-job-search-agent!")
    result=agent.invoke({
        "messages": HumanMessage(content="Search for 3 job postings for an ai engineer using langchain in cairo on linkedin and list their details")
        })
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
