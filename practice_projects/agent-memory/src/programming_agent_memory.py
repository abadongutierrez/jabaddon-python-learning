from letta_client import Letta

client = Letta(base_url="http://localhost:8283")

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
    elif message.message_type == "usage_statistics": 
        # for streaming specifically, we send the final chunk that contains the usage statistics 
        print(f"Usage: [{message}]")
    else: 
        print(message)
    print("-----------------------------------------------------")
    
agent_state = client.agents.create(
    memory_blocks=[
        {
          "label": "human",
          "value": "The human's name is Bob the Builder."
        },
        {
          "label": "persona",
          "value": "My name is Sam, the all-knowing sentient AI."
        }
    ],
    model="openai/gpt-4o-mini",
    embedding="openai/text-embedding-3-small"
)

blocks = client.agents.blocks.list(
    agent_id=agent_state.id,
)

print("Agent Memory Blocks:")
for block in blocks:
    print(block.label + ": " + block.value)

# Note: Replace the block_id with the id from the cell above.
block_id=blocks[0].id

blocks = client.blocks.retrieve(block_id)
print("Retrieved Block:")
print(blocks.label + ": " + blocks.value)

human_block = client.agents.blocks.retrieve(
    agent_id=agent_state.id,
    block_label="human",
)
print("Human Block from Agent:")
print(human_block.label + ": " + human_block.value)

template = client.agents.core_memory.retrieve(
    agent_id=agent_state.id
).prompt_template
print("Core Memory Prompt Template:")
print(template)

# Accesing state with tools
def get_agent_id(agent_state: "AgentState"):
    """
    Query your agent ID field
    """
    return agent_state.id

# create tool
get_id_tool = client.tools.upsert_from_function(func=get_agent_id)

agent_state = client.agents.create(
    memory_blocks=[],
    model="openai/gpt-4o-mini",
    embedding="openai/text-embedding-3-small",
    tool_ids=[get_id_tool.id]
)

response_stream = client.agents.messages.create_stream(
    agent_id=agent_state.id,
    messages=[
        {
            "role": "user",
            "content": "What is your agent id?" 
        }
    ]
)

for chunk in response_stream:
    print_message(chunk)
    
# Custom task queue memory

# Tool to push to task queue
def task_queue_push(agent_state: "AgentState", task_description: str):
    """
    Push to a task queue stored in core memory.

    Args:
        task_description (str): A description of the next task you must accomplish.

    Returns:
        Optional[str]: None is always returned as this function
        does not produce a response.
    """

    from letta_client import Letta
    import json

    client = Letta(base_url="http://localhost:8283")

    block = client.agents.blocks.retrieve(
        agent_id=agent_state.id,
        block_label="tasks",
    )
    tasks = json.loads(block.value)
    tasks.append(task_description)

    # update the block value
    client.agents.blocks.modify(
        agent_id=agent_state.id,
        value=json.dumps(tasks),
        block_label="tasks"
    )
    return None

# Tool to pop from task queue
def task_queue_pop(agent_state: "AgentState"):
    """
    Get the next task from the task queue 
 
    Returns:
        Optional[str]: Remaining tasks in the queue
    """

    from letta_client import Letta
    import json 

    client = Letta(base_url="http://localhost:8283") 

    # get the block 
    block = client.agents.blocks.retrieve(
        agent_id=agent_state.id,
        block_label="tasks",
    )
    tasks = json.loads(block.value) 
    if len(tasks) == 0: 
        return None
    task = tasks[0]

    # update the block value 
    remaining_tasks = json.dumps(tasks[1:])
    client.agents.blocks.modify(
        agent_id=agent_state.id,
        value=remaining_tasks,
        block_label="tasks"
    )
    return f"Remaining tasks {remaining_tasks}"

task_queue_pop_tool = client.tools.upsert_from_function(
    func=task_queue_pop
)
task_queue_push_tool = client.tools.upsert_from_function(
    func=task_queue_push
)

import json

task_agent = client.agents.create(
    system=open("task_queue_system_prompt.txt", "r").read(),
    memory_blocks=[
        {
          "label": "tasks",
          "value": json.dumps([])
        }
    ],
    model="openai/gpt-4o-mini-2024-07-18",
    embedding="openai/text-embedding-3-small", 
    tool_ids=[task_queue_pop_tool.id, task_queue_push_tool.id], 
    include_base_tools=False, 
    tools=["send_message"]
)

for tool in task_agent.tools:
    print("Task Agent Tool: " + tool.name)
    
block = client.agents.blocks.retrieve(task_agent.id, block_label="tasks").value
print("Initial Task Queue Block: " + block)

response_stream = client.agents.messages.create_stream(
    agent_id=task_agent.id,
    messages=[
        {
            "role": "user",
            "content": "Add 'start calling me Charles' and "
            + "'tell me a haiku about my name' as two seperate tasks."
        }
    ]
)

for chunk in response_stream:
    print_message(chunk)
    
# In case agent did not process both tasks, we can check the task queue block
response_stream = client.agents.messages.create_stream(
    agent_id=task_agent.id,
    messages=[
        {
            "role": "user",
            "content": "Complete your tasks"
        }
    ]
)

for chunk in response_stream:
    print_message(chunk)
    
block_value = client.agents.blocks.retrieve(block_label="tasks", agent_id=task_agent.id).value
print("Final Task Queue Block: " + block_value)