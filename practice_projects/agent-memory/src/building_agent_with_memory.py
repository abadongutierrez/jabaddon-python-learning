from letta_client import Letta

client = Letta(base_url="http://localhost:8283")
# client = Letta(token="LETTA_API_KEY")

def print_message(message):
    if message.message_type == "reasoning_message":
        print("🧠 Reasoning: " + message.reasoning)
    elif message.message_type == "assistant_message":
        print("🤖 Agent: " + message.content)
    elif message.message_type == "tool_call_message":
        print("🔧 Tool Call: " + message.tool_call.name + "\n" + message.tool_call.arguments)
    elif message.message_type == "tool_return_message":
        print("🔧 Tool Return: " + message.tool_return)
    elif message.message_type == "user_message":
        print("👤 User Message: " + message.content)
        
# Creating an agent with memory blocks
agent_state = client.agents.create(
    name="simple_agent",
    memory_blocks=[
        {
          "label": "human",
          "value": "My name is Charles",
          "limit": 10000 # character limit
        },
        {
          "label": "persona",
          "value": "You are a helpful assistant and you always use emojis"
        }
    ],
    model="openai/gpt-4o-mini-2024-07-18",
    embedding="openai/text-embedding-3-small"
)

# send a message to the agent
response = client.agents.messages.create(
    agent_id=agent_state.id,
    messages=[
        {
            "role": "user",
            "content": "hows it going????"
        }
    ]
)

# if we want to print the messages
for message in response.messages:
    print_message(message)
    
# if we want to print the usage stats
print(response.usage.completion_tokens)
print(response.usage.prompt_tokens)
print(response.usage.step_count)

# Understanding the agent state
print(agent_state.system)

print([t.name for t in agent_state.tools])

# Lets give agent new information
response = client.agents.messages.create(
    agent_id=agent_state.id,
    messages=[
        {
            "role": "user",
            "content": "My name i actually Rafael"
        }
    ]
)

for message in response.messages:
    print_message(message)
    
v = client.agents.blocks.retrieve(
    agent_id=agent_state.id,
    block_label="human"
).value
print("Updated human block value: " + v)

# Understanding archival memory
passages = client.agents.passages.list(
    agent_id=agent_state.id
)
print("Agent passages:")
print(passages)

response = client.agents.messages.create(
    agent_id=agent_state.id,
    messages=[
        {
            "role": "user",
            "content": "Save the information that 'bob loves cats' to archival"
        }
    ]
)

# if we want to print the messages
for message in response.messages:
    print_message(message)
    
passages = client.agents.passages.list(
    agent_id=agent_state.id,
)
[passage.text for passage in passages]
print("Agent passages after adding new passage:")
print(passages)

# Explicitly creating archival memory
client.agents.passages.create(
    agent_id=agent_state.id,
    text="bob loves orange cats"
)

# send a message to the agent
response = client.agents.messages.create(
    agent_id=agent_state.id,
    messages=[
        {
            "role": "user",
            "content": "What animals do I like? Search archival."
        }
    ]
)

for message in response.messages:
    print_message(message)

# send a message to the agent
response = client.agents.messages.create(
    agent_id=agent_state.id,
    messages=[
        {
            "role": "user",
            "content": "What animals do Bob like?"
        }
    ]
)

for message in response.messages:
    print_message(message)
