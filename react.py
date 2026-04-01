from dotenv import load_dotenv
import os

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain.tools import tool
from langchain_tavily import TavilySearch

@tool
def triple(num:float) -> float:
    """Triples the input number."""
    return num * 3

tools = [TavilySearch(max_results=3), triple]

llm = ChatOpenAI(model="openai/gpt-3.5-turbo",
                 base_url = "https://openrouter.ai/api/v1",
                 api_key=os.getenv("OPENROUTER_API_KEY"),
                 temperature=0.3).bind_tools(tools)



