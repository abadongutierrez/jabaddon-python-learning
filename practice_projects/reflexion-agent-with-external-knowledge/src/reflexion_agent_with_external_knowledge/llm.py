"""LLM configuration for the reflexion agent."""

import os
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4.1-nano",
    api_key=os.getenv("OPENAI_API_KEY")
)