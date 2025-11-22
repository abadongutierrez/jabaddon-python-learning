import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

# Load environment variables from .env file
load_dotenv()

# Initialize the Ollama chat model with cloud configuration
llm = ChatOllama(
    model="gpt-oss:120b-cloud",
    base_url="https://ollama.com",
    headers={
        "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
    }
)

# Create a message asking about being a good Data Scientist
messages = [
    HumanMessage(content="How to be good Data Scientist?")
]

# Stream the response
print("Response: ", end="", flush=True)
for chunk in llm.stream(messages):
    print(chunk.content, end="", flush=True)
print()  # New line at the end
