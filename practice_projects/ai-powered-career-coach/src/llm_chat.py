import os
from xml.parsers.expat import model
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import gradio as gr

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

# Function to generate a response from the model
def generate_response(prompt_txt):
    messages = [{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt_txt
            },
        ]
    }]   
    generated_response = llm.invoke(messages)
    return generated_response.content

# Create Gradio interface
chat_application = gr.Interface(
    fn=generate_response,
    flagging_mode="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output", lines=10, max_lines=20, show_copy_button=True),
    title="Ollama Cloud Chatbot",
    description="Ask any question and the chatbot will try to answer."
)
# Launch the app
chat_application.launch()