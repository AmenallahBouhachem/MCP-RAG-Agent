import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def main():
    load_dotenv()

    
    config = {
      
  "mcpServers": {
       "amenT": {
            "type": "stdio",
            "command": "uv",
            "args": [
                "--directory",
                "C:\\Users\\Amen Allah\\OneDrive\\Bureau\\MCP-RAG-Agent\\rag",
                "run",
                "server.py"
            ]
        }
  }


    }

    client = MCPClient.from_dict(config)
    

    llm = ChatGroq(model="qwen-qwq-32b", api_key=os.getenv("GROQ_API_KEY"))

    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    result = await agent.run(
        " I have a headache can you tell me what are the possible diseases that I might have?",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())