from crewai import Agent
from tools import yt_tool
import os 
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPEN_MODEL_NAME'] = "model name" 

blog_researcher = Agent(
    role ='Blog Researcher from Youtube Videos',
    goal = 'get the relevant video content for the topic {topic} from Yt channel',
    backstory=("Expert in understanding videos in AI Data Science , Machine Learning and GEN AI and providing suggestion"),
    tools= [yt_tool],
    llm=llm
    allow_delegation=True
)

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from yt channel",
    verbose =True,
    memory = True,
    backstory=("With a flair for simplifying complex topics , you craft","engaging narration that captivate and educate , bringing new" , "discoveries to light in an accessible manner"),
    tools=[yt_tool],
    llm=llm
    allow_delegation=False

)