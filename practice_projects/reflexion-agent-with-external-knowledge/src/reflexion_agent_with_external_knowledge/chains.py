"""LangChain chains for the reflexion agent."""

from .llm import llm
from .prompts import first_responder_prompt, revisor_prompt
from .models import AnswerQuestion, ReviseAnswer


# Initial chain for generating first response with reflection
initial_chain = first_responder_prompt | llm.bind_tools(tools=[AnswerQuestion])


# Revisor chain for revising answers based on search results
revisor_chain = revisor_prompt | llm.bind_tools(tools=[ReviseAnswer])
