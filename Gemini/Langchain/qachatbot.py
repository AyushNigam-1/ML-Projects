import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama
import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] ="true"
os.environ['LANGCHAIN_PROJECT'] = "Simple Q&A Chatbot with OLLAMA"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant, Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,engine):
    llm = Ollama(model=engine)
    output_parser = StrOutputParser()
    chain =  prompt|llm|output_parser
    answer=chain.invoke({"question":question})
    return answer

engine = st.sidebar.selectbox("Select Engine",['gemma2:2b'])

st.write("Go Ahead And Ask Anything")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input,engine)
    st.write(response)
else:
    st.write("Please provide the user input")