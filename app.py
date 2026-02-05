import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain import hub
from dotenv import load_dotenv
import os

# 1. Load your API key from the .env file
load_dotenv()

# Streamlit Page Setup
st.set_page_config(page_title="Conversational Knowledge Bot", page_icon="🤖")
st.title("🤖 Conversational Knowledge Bot")

# 2. Initialize the LLM (Using 2026 stable gpt-4o-mini)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 3. Setup the Tool (DuckDuckGo Search)
search_tool = DuckDuckGoSearchRun()
tools = [search_tool]

# 4. Pull the modern ReAct prompt from LangChain Hub
# This replaces the old hidden logic in initialize_agent
prompt = hub.pull("hwchase17/react")

# 5. Initialize Memory in Session State
# This ensures history persists during Streamlit's reruns
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history", 
        return_messages=True
    )

# 6. Construct the Modern Agent and Executor
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    memory=st.session_state.memory, 
    verbose=True,
    handle_parsing_errors=True
)

# 7. Chat UI Display Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 8. User Input and Response Generation
if user_input := st.chat_input("Ask a question (e.g., 'Who is the CEO of OpenAI?')"):
    # Store and display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate and display bot response
    with st.chat_message("assistant"):
        # The new invoke method is the 2026 standard for running agents
        response = agent_executor.invoke({"input": user_input})
        bot_output = response["output"]
        st.markdown(bot_output)
    
    st.session_state.messages.append({"role": "assistant", "content": bot_output})
