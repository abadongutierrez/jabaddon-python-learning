"""Pydantic models for the reflexion agent."""

from typing import List, Annotated, TypedDict
from pydantic import BaseModel, Field
from langgraph.graph.message import add_messages, AnyMessage


class Reflection(BaseModel):
    """Self-critique of an answer."""
    missing: str = Field(description="What information is missing")
    superfluous: str = Field(description="What information is unnecessary")


class AnswerQuestion(BaseModel):
    """Initial answer to a question with reflection and search queries."""
    answer: str = Field(description="Main response to the question")
    reflection: Reflection = Field(description="Self-critique of the answer")
    search_queries: List[str] = Field(description="Queries for additional research")


class ReviseAnswer(AnswerQuestion):
    """Revise your original answer to your question."""
    references: List[str] = Field(description="Citations motivating your updated answer.")


class MessagesState(TypedDict):
    """State for the reflexion agent graph."""
    messages: Annotated[list[AnyMessage], add_messages]
