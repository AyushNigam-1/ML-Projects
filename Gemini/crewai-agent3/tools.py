from crewai_tools import YoutubeChannelSearchTool
from langchain_community.llms import Ollama
# Initialize Ollama LLM
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="@krishnaik06",
)