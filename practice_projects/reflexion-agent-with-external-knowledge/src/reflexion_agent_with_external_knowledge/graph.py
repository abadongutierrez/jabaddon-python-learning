"""LangGraph state graph for the reflexion agent."""

from langgraph.graph import END, StateGraph
from langchain_core.messages import ToolMessage

from .models import MessagesState
from .chains import initial_chain, revisor_chain
from .tools import execute_tools


# Configuration
MAX_ITERATIONS = 4


def event_loop(state: MessagesState) -> str:
    """Determine whether to continue the loop or end.

    Args:
        state: Current message state

    Returns:
        Next node to visit or END
    """
    messages = state["messages"]
    count_tool_visits = sum(isinstance(item, ToolMessage) for item in messages)
    num_iterations = count_tool_visits
    if num_iterations >= MAX_ITERATIONS:
        return END
    return "execute_tools"


def respond_node(state: MessagesState) -> MessagesState:
    """Initial response node using the initial chain.

    Args:
        state: Current message state

    Returns:
        Updated state with initial response
    """
    messages = state["messages"]
    response = initial_chain.invoke({"messages": messages})
    return {"messages": [response]}


def revisor_node(state: MessagesState) -> MessagesState:
    """Revisor node that revises answers based on search results.

    Args:
        state: Current message state

    Returns:
        Updated state with revised response
    """
    messages = state["messages"]
    response = revisor_chain.invoke({"messages": messages})
    return {"messages": [response]}


def build_graph() -> StateGraph:
    """Build and compile the reflexion agent graph.

    Returns:
        Compiled state graph ready for execution
    """
    graph = StateGraph(MessagesState)

    # Add nodes
    graph.add_node("respond", respond_node)
    graph.add_node("execute_tools", execute_tools)
    graph.add_node("revisor", revisor_node)

    # Add edges
    graph.add_edge("respond", "execute_tools")
    graph.add_edge("execute_tools", "revisor")
    graph.add_conditional_edges("revisor", event_loop)

    # Set entry point
    graph.set_entry_point("respond")

    return graph.compile()


# Create the compiled graph app
app = build_graph()
