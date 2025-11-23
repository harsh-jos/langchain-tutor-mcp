import asyncio
import streamlit as st 
from mcp_use import MCPClient, MCPAgent 

async def generate_answer(query, model: str, API_KEY: str):
    llm = None
    if model=="Google":
        model = "gemini-2.5-flash"

        from langchain_google_genai import ChatGoogleGenerativeAI
        llm = ChatGoogleGenerativeAI(model=model, google_api_key=API_KEY)

    else:
        model = "llama-3.3-70b-versatile"

        from langchain_groq import ChatGroq
        llm = ChatGroq(model=model, groq_api_key=API_KEY)

    client = MCPClient.from_config_file("mcp.json")
    agent = MCPAgent(llm=llm, client=client, max_steps=10)

    result = await agent.run(query,  max_steps=10)
    return result


if __name__ == "__main__":
    st.set_page_config(page_title="Langchain Tutor", page_icon="📚")
    st.title("Langchain Tutor")

    with st.sidebar:
        model = st.radio(
            "Select the Language Model",
            ["Google", "Groq-Llama"]
        )
        API_KEY = st.text_input("Enter the API key", type="password")

    if model and API_KEY:
        
        query = st.chat_input(placeholder="Enter your message")
        if query:
            st.chat_message("user").write(query)
            result = asyncio.run(generate_answer(query, model, API_KEY))
            if result:
                st.chat_message("assistant").write(result)
    