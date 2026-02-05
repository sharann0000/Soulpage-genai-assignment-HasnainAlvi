import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import os

# Load API Keys
load_dotenv()

# Streamlit Page Configuration
st.set_page_config(page_title="Knowledge Bot", layout="centered")
st.title("🤖 Conversational Knowledge Bot")

# 1. Initialize the LLM
# You can use "gpt-3.5-turbo" or "gpt-4o-mini"
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 2. Setup External Search Tool (DuckDuckGo)
search_tool = DuckDuckGoSearchRun()
tools = [search_tool]

# 3. Setup Memory in Streamlit Session State
# This ensures history isn't lost when the app re-runs
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history", 
        return_messages=True
    )

# 4. Initialize the Agent
agent_chain = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=st.session_state.memory
)

# 5. Chat UI Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask me anything!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # The agent uses memory and tools to answer
        response = agent_chain.run(input=prompt)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
