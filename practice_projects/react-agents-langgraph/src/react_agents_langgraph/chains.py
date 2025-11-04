from react_agents_langgraph.llm import llm
from react_agents_langgraph.prompts import chat_prompt
from react_agents_langgraph.tools import tools

model_react = chat_prompt | llm.bind_tools(tools)

