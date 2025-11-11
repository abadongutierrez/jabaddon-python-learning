from letta_client import Letta

client = Letta(base_url="http://localhost:8283")

def print_message(message):
    if message.message_type == "reasoning_message":
        print("🧠 Reasoning: " + message.reasoning)
    elif message.message_type == "assistant_message":
        print("🤖 Agent: " + message.content)
    elif message.message_type == "tool_call_message":
        print("🔧 Tool Call: " + message.tool_call.name +  \
              "\n" + message.tool_call.arguments)
    elif message.message_type == "tool_return_message":
        print("🔧 Tool Return: " + message.tool_return)
    elif message.message_type == "user_message":
        print("👤 User Message: " + message.content)
    elif message.message_type == "system_message":
        print(" System Message: " + message.content)
    elif message.message_type == "usage_statistics":
        # for streaming specifically, we send the final
        # chunk that contains the usage statistics
        print(f"Usage: [{message}]")
        return
    print("-----------------------------------------------------")
    
company_description = "The company is called AgentOS " \
+ "and is building AI tools to make it easier to create " \
+ "and deploy LLM agents."

company_block = client.blocks.create(
    value=company_description,
    label="company",
    limit=10000 # character limit
)
print("Created Company Block:")
print(company_block.id, company_block.value)

# Tool to draft candidate email
def draft_candidate_email(content: str):
    """
    Draft an email to reach out to a candidate.

    Args:
        content (str): Content of the email
    """
    return f"Here is a draft email: {content}"

# Upsert the tool
draft_email_tool = client.tools.upsert_from_function(func=draft_candidate_email)

outreach_persona = (
    "You are responsible for drafting emails "
    "on behalf of a company with the draft_candidate_email tool. "
    "Candidates to email will be messaged to you. "
)

outreach_agent = client.agents.create(
    name="outreach_agent",
    memory_blocks=[
        {"label": "persona", "value": outreach_persona}
    ],
    model="openai/gpt-4o-mini-2024-07-18",
    embedding="openai/text-embedding-ada-002",
    tools=[draft_email_tool.name],
    block_ids=[company_block.id]
)

# Reject tool
def reject(candidate_name: str): 
    """ 
    Reject a candidate. 

    Args: 
        candidate_name (str): The name of the candidate
    """
    return

# Upsert the tool
reject_tool = client.tools.upsert_from_function(func=reject)

# Creating a persona for evaluating candidate
skills = "Front-end (React, Typescript) or software engineering skills"

eval_persona = (
    f"You are responsible for evaluating candidates. "
    f"Ideal candidates have skills: {skills}. "
    "Reject bad candidates with your reject tool. "
    f"Send strong candidates to agent ID {outreach_agent.id}. "
    "You must either reject or send candidates to the other agent. "
)

eval_agent = client.agents.create(
    name="eval_agent",
    memory_blocks=[
        {"label": "persona", "value": eval_persona}
    ],
    model="openai/gpt-4o-mini-2024-07-18",
    embedding="openai/text-embedding-ada-002",
    tool_ids=[reject_tool.id],
    tools=['send_message_to_agent_and_wait_for_reply'],
    include_base_tools=False,
    block_ids=[company_block.id],
    tool_rules = [
        {
            "type": "exit_loop",
            "tool_name": "send_message_to_agent_and_wait_for_reply"
        }
    ]
)
print("Eval Agent Tools: " + str([t.name for t in eval_agent.tools]))

# Read candidate resume and sending to eval agent
resume = open("resumes/tony_stark.txt", "r").read()

response = client.agents.messages.create_stream(
    agent_id=eval_agent.id,
    messages=[
        {
            "role": "user",
            "content": f"Evaluate: {resume}"
        }
    ]
)

print("Eval Agent Response Stream:")
for message in response:
    print_message(message)

# print messages for `outreach_agent`
print("Outreach Agent Messages:")
for message in client.agents.messages.list(agent_id=outreach_agent.id)[1:]: 
    print_message(message)

response = client.agents.messages.create_stream(
    agent_id=outreach_agent.id,
    messages=[
        {
            "role": "user",
            "content": "The company has rebranded to Letta"
        }
    ]
)
for message in response:
    print_message(message)

value = client.agents.blocks.retrieve(
    agent_id=eval_agent.id, 
    block_label="company"
).value

print("Updated Company Block in Eval Agent: " + value)

value = client.agents.blocks.retrieve(
    agent_id=outreach_agent.id, 
    block_label="company"
).value

print("Updated Company Block in Outreach Agent: " + value)

# ------
# Multi-agent groups
# ------

def print_message_multiagent(message):  
    if message.message_type == "reasoning_message": 
        print(f"🧠 Reasoning ({message.name}): " + message.reasoning) 
    elif message.message_type == "assistant_message": 
        print(f"🤖 Agent ({message.name}): " + message.content) 
    elif message.message_type == "tool_call_message": 
        print(f"🔧 Tool Call ({message.name}): " + message.tool_call.name + "\n" + message.tool_call.arguments)
    elif message.message_type == "tool_return_message": 
        print(f"🔧 Tool Return ({message.name}): " + message.tool_return)
    elif message.message_type == "user_message": 
        print("👤 User Message: " + message.content)
    elif message.message_type == "usage_statistics": 
        # for streaming specifically, we send the final chunk that contains the usage statistics 
        print(f"Usage: [{message}]")
        return 
    print("-----------------------------------------------------")
    
# create the outreach agent 
outreach_agent = client.agents.create(
    name="outreach_agent",
    memory_blocks=[
        { "label": "persona", "value": outreach_persona}
    ],
    model="openai/gpt-4o-mini-2024-07-18",
    embedding="openai/text-embedding-ada-002",
    tool_ids=[draft_email_tool.id], 
    block_ids=[company_block.id]
)

# create the evaluation agent 
eval_agent = client.agents.create(
    name="eval_agent",
    memory_blocks=[
        { "label": "persona", "value": eval_persona}
    ],
    model="openai/gpt-4o-mini-2024-07-18",
    embedding="openai/text-embedding-ada-002",
    tool_ids=[reject_tool.id],
    block_ids=[company_block.id]
)

"""
Round-Robin Group
"""
round_robin_group = client.groups.create(
    description="This team is responsible for recruiting candidates.",
    agent_ids=[eval_agent.id, outreach_agent.id],
)

# Messaging an agent group
resume = open("resumes/spongebob_squarepants.txt", "r").read()
response_stream = client.groups.messages.create_stream(
    group_id=round_robin_group.id,
    messages=[
       {"role": "user", "content": f"Evaluate: {resume}"}
    ]
)

print("Round-Robin Group Response Stream:")
for message in response_stream: 
    print_message_multiagent(message)