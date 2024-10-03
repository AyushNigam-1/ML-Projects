from crewai import Crew , Process ,crew
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task
from langchain_community.llms import Ollama
llm = Ollama(model="llama3.2:latest")
crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
    llm=llm
)


result = crew.kickoff(inputs={'topic':'AI VS ML VS DL VS Data Science'})