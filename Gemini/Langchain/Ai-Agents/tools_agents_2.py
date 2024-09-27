import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper , WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun , WikipediaQueryRun , DuckDuckGoSearchRun , YouTubeSearchTool
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from langchain.llms.ollama import Ollama 
from dotenv import load_dotenv

arxiv_wrapper = ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

youtube = YouTubeSearchTool(name="Youtube")

search = DuckDuckGoSearchRun(name="Search")

st.title("Langchain - Chat with Search")

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key",key="Password")

if "message" not in st.session_state:
    st.session_state['messages'] = [
        {"role":"assistant","content":"Hi , I'm a chatbot who can search the web , How can I help you"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if prompt:= st.chat_input(placeholder="What is machine earning?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    # llm = ChatGroq(groq_api_key=api_key,model="Llama3-8b-8192",streaming=True)
    llm = Ollama(model="llama3.2:3b-instruct-q8_0")
    tools = [search,arxiv,wiki,youtube]

    search_agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

    with st.chat_message('assistant'):
        st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages,callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant',"content":response})
        st.write(response)