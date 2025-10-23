"""Reflexion agent with external knowledge integration.

This module implements a deep research agent using reflection techniques
to answer questions, critique answers, and revise them based on external research.
"""

from .llm import llm
from .models import Reflection, AnswerQuestion, ReviseAnswer, MessagesState
from .prompts import (
    first_responder_prompt,
    revisor_prompt,
    prompt_template,
    FIRST_INSTRUCTION,
    REVISE_INSTRUCTIONS,
)
from .chains import initial_chain, revisor_chain
from .tools import tavily_tool, execute_tools
from .graph import app, build_graph, MAX_ITERATIONS


__all__ = [
    # LLM
    "llm",
    # Models
    "Reflection",
    "AnswerQuestion",
    "ReviseAnswer",
    "MessagesState",
    # Prompts
    "first_responder_prompt",
    "revisor_prompt",
    "prompt_template",
    "FIRST_INSTRUCTION",
    "REVISE_INSTRUCTIONS",
    # Chains
    "initial_chain",
    "revisor_chain",
    # Tools
    "tavily_tool",
    "execute_tools",
    # Graph
    "app",
    "build_graph",
    "MAX_ITERATIONS",
]
