from mcp.server.fastmcp import FastMCP
from llama_index.core.postprocessor.llm_rerank import LLMRerank
from llama_index.core.schema import QueryBundle
import os 
from llama_index.llms.groq import Groq
from rag import get_index
from dotenv import load_dotenv
load_dotenv()

os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN')
mcp = FastMCP(
    host='127.0.0.1',
    port=8000,
    timeout =30,
)

@mcp.tool()
def rag_tool(query: str) -> str:
    """
    Retrieve the most relevant documents from the machine learning
    collection. Use this tool when the user asks about ML.

    Input:
        query: str -> The user query to retrieve the most relevant documents

    Output:
        context: str -> most relevant documents retrieved from a vector DB
    """
    llm = Groq(model="llama-3.3-70b-versatile", api_key=os.getenv('GROQ_API_KEY'))
    reranker = LLMRerank(
            choice_batch_size=5, top_n=5, llm=llm
        )
    index = get_index()
    query_engine = index.as_query_engine(node_postprocessors=[reranker], response_mode="tree")
    context = query_engine.retrieve(QueryBundle(query=query))
    context = context[0].node.text if context else "No relevant documents found."

    return context
