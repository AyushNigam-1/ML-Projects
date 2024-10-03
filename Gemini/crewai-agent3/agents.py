from crewai import Agent
from tools import yt_tool
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
import os

os.environ['OPEN_API_KEY'] = "demo-111"
llm = ChatOpenAI(
    model="llama3.2:latest",
    base_url="http://localhost:11434/v1"
)

blog_researcher = Agent(
    role = "Blog Researcher from Youtube Videos",
    goal = "get the relevant video for the topic {topic} from yt channel",
    verbose = True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science , Machine Learning and GEN AI and providing suggestion "
    ),
    allow_delegation=True,
    tools=[yt_tool],
    llm=llm

)

blog_writer = Agent(
    role="Blog Writer",
    goal = "Narrate Compelling tech stories about the video {topic} from YT channel",
    verbose=True,
    memory=True,
    backstory=(
        "WIth a flair for simplifying complex topic , you craft"
        "engaging narratives that captivate and educate , bringing new"
        "discoveries to light in a accessibke manner"
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm
)