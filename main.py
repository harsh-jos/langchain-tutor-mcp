import os
import asyncio
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
from langchain_groq import ChatGroq

async def main():
    load_dotenv()

    client = MCPClient.from_config_file(os.path.join("mcp.json"))

    groq_api_key = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.3-70b-versatile")

    agent = MCPAgent(llm=llm, client=client, max_steps=10)

    result = await agent.run(
        "What is the biggest update for Langchain philosophy in v1.0"
    )
    print(f"\nResult: {result}")

    # query = "What is the biggest update for Langchain philosophy in v1.0"
    # async for chunk in agent.stream(query):
    #     print(chunk, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
