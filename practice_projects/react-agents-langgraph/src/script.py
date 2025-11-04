# ReAct stands for Reasoning and Acting, a framework that combines reasoning and action in language models.

# Reasoning:  The agent thinks through the problem step-by-step, maintaining an internal dialogue about what it needs to do.
# Acting: The agent can use external tools (search engines, calculators, databases, etc.) to gather information or perform actions.
# Observing: The agent processes the results of its actions and incorporates that information into its reasoning.

# Think -> Act -> Observe -> Think -> Act -> Observe ... until a final answer is reached.

import json
from react_agents_langgraph import search_tool
from react_agents_langgraph import AgentState
from langchain_core.messages import HumanMessage, ToolMessage
from langgraph.graph.message import add_messages
from react_agents_langgraph.chains import model_react
from react_agents_langgraph.tools import tools_by_name

result = search_tool.invoke("what's the weather like in Tokyo today?")
print(result)

# Demo state management
state: AgentState = {"messages": []}
state["messages"] = add_messages(state["messages"], [
    HumanMessage(content="What's the capital of France?")
])
print("After greeting:", state["messages"])

# Manual ReAct execution (understanding the flow)

# Step 1: ReAct reasoning
dummy_state: AgentState = {"messages": [
    HumanMessage(content="What's the weather like in Zurich, and what should I wear based on the temperature?")
]}

response = model_react.invoke({ "scratch_pad": dummy_state["messages"] })

# Update state with the model's response
dummy_state["messages"] = add_messages(dummy_state["messages"], [response])

print("----- ReAct Execution -----")
print("ReAct response:", response)
print("----- Updated State -----")
print("Updated state messages:", dummy_state["messages"])

# Step 2: Tool execution
tool_call = response.tool_calls[-1]
print("----- Tool Call -----")
print("Tool to call:", tool_call)

tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
print("Tool result:", tool_result)

tool_message = ToolMessage(
    content = json.dumps(tool_result),
    name = tool_call["name"],
    tool_call_id = tool_call["id"]
)

# tool_message is added back to the state
dummy_state["messages"] = add_messages(dummy_state["messages"], [tool_message])

print("----- Updated State -----")
print("Updated state messages:", dummy_state["messages"])

# Step 3: Processing results and next actions
response = model_react.invoke({ "scratch_pad": dummy_state["messages"] })
dummy_state["messages"] = add_messages(dummy_state["messages"], [response])

if response.tool_calls:
    tool_call = response.tool_calls[0]
    tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
    tool_message = ToolMessage(
        content = json.dumps(tool_result),
        name = tool_call["name"],
        tool_call_id = tool_call["id"]
    )
    dummy_state["messages"] = add_messages(dummy_state["messages"], [tool_message])

print("----- Updated State -----")
print("Final state messages:", dummy_state["messages"])

# Step 4: Final response generation
response = model_react.invoke({ "scratch_pad": dummy_state["messages"] })
print("Final response generated:", response.content is not None)
print("More tools needed:", bool(response.tool_calls))


