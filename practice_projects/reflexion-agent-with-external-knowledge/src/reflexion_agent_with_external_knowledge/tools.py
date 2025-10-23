"""External tools for the reflexion agent."""

import json
from langchain_tavily import TavilySearch
from .models import MessagesState


# Initialize Tavily search tool
tavily_tool = TavilySearch(max_results=1)


def execute_tools(state: MessagesState) -> MessagesState:
    """Execute search tools based on the AI's search queries.

    Args:
        state: Current message state containing all messages

    Returns:
        Updated state with tool messages containing search results
    """
    from langchain_core.messages import ToolMessage

    messages = state["messages"]
    last_ai_message = messages[-1]
    tool_messages = []

    # Check if the message has tool_calls attribute and if it's not empty
    if hasattr(last_ai_message, 'tool_calls') and last_ai_message.tool_calls:
        for tool_call in last_ai_message.tool_calls:
            if tool_call["name"] in ["AnswerQuestion", "ReviseAnswer"]:
                call_id = tool_call["id"]
                search_queries = tool_call["args"].get("search_queries", [])
                query_results = {}
                for query in search_queries:
                    result = tavily_tool.invoke(query)
                    query_results[query] = result
                tool_messages.append(ToolMessage(
                    content=json.dumps(query_results),
                    tool_call_id=call_id)
                )
    return {"messages": tool_messages}
