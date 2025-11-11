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


# Get or create datasource
try:
    source = client.sources.create(
        name="employee_handbook",
        embedding="openai/text-embedding-3-small"
    )
    print("Created Source:")
    print(source.id)
except Exception as e:
    if "UniqueConstraintViolationError" in str(e) or "duplicate key" in str(e):
        print("Source already exists, retrieving it...")
        sources = client.sources.list()
        source = next((s for s in sources if s.name == "employee_handbook"), None)
        if source:
            print("Found existing source:")
            print(source.id)
        else:
            raise Exception("Source exists but couldn't be retrieved")
    else:
        raise

# upload data
import time

file_metadata = client.sources.files.upload(
    source_id=source.id,
    file=open("handbook.pdf", "rb")
)
print("Uploaded File:")
print(file_metadata.id)

# Wait for file processing by checking passages
print("Waiting for processing to complete...")
passages_count = 0
max_wait = 60  # Maximum wait time in seconds
elapsed = 0

while passages_count == 0 and elapsed < max_wait:
    time.sleep(2)
    elapsed += 2
    passages = client.sources.passages.list(source_id=source.id)
    passages_count = len(passages)
    print(f"Passages found: {passages_count}")

if passages_count > 0:
    print("Processing completed!")
else:
    print("Warning: Processing may still be ongoing or failed")

passages = client.sources.passages.list(
    source_id=source.id,
)
print("Source Passages: " + str(len(passages)))
for passage in passages:
    print(passage.text[:10] + "...")

agent_state = client.agents.create(
    memory_blocks=[
        {
          "label": "human",
          "value": "My name is Sarah"
        },
        {
          "label": "persona",
          "value": "You are a helpful assistant"
        }
    ],
    model="openai/gpt-4o-mini-2024-07-18",
    embedding="openai/text-embedding-3-small"
)

agent_state = client.agents.sources.attach(
    agent_id=agent_state.id, 
    source_id=source.id
)

client.agents.sources.list(agent_id=agent_state.id)
passages = client.agents.passages.list(agent_id=agent_state.id)
print("Agent Passages: " + str(len(passages)))

response = client.agents.messages.create(
    agent_id=agent_state.id,
    messages=[
        {
            "role": "user",
            "content": "Search archival for our company's vacation policies"
        }
    ]
)
for message in response.messages:
    print_message(message)