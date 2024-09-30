import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain , LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool , initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

st.set_page_config(page_title="Text to Math Problem Solver And Data Search Assistant",page_icon="$")

groq_api_key = st.sidebar.text_input(label="Groq API Key",type="password")

if not groq_api_key:
    st.info("Please add your Groq API Key to continue")
    st.stop()

llm = ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

wikipedia_wrapper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="This tool allows you to search Wikipedia for relevant information on a wide variety of topics. It is useful when you need detailed explanations, historical facts, or general knowledge from the world's largest online encyclopedia"
)

math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="This tool helps you perform mathematical calculations, including basic arithmetic, algebra, and more advanced mathematical operations. It's ideal for solving math problems quickly and accurately."
)

prompt = """
You are agent tasked for solving mathematicak question
Question:{question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=['question'],
    template=prompt
)
chain = LLMChain(llm=llm,prompt=prompt_template)

resoning_tool=  Tool(
    name="Resoning tool",
    func=chain.run,
    description="This tool is designed to assist with logical reasoning and problem-solving tasks. It processes and analyzes complex questions to provide well-thought-out explanations or solutions, making it useful for tackling math problems, logical puzzles, and other analytical challenges"
)

assistant_agent = initialize_agent(
    tools=[wikipedia_tool , resoning_tool , calculator],
    llm=llm,
     agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
     handle_parsing_error=True
)

if "messages" not in st.session_state:
    st.session_state['messages'] = [
        {'role':'assistant','content':'I am a math chatbot who can answer all your math question'}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

# def generate_response(question):
#     response=assistant_agent.invoke({'input':question})
#     return response

question = st.text_area("Enter your question","I have 4 bananas and i ate 3 banans , now how many bananas are there ")

if st.button("Find My Answer"):
    if question:
        with st.spinner("Generate Response"):
            st.session_state.messages.append({'role':'user','content':question})
            st.chat_message('user').write(question)
            st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts = False)
            response = assistant_agent.run(st.session_state.messages,callbacks=[st_cb])
            st.session_state.messages.append({'role':'assitant','content':response})
            st.write("### Response : ")
            st.success(response)
    else:
        st.warning("Please enter input")
