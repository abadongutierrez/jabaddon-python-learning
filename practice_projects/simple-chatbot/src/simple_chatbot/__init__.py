# Export public API from the chatbot module
from simple_chatbot.chatbot import (
    chat,
    get_conversation_history,
    clear_history,
)

# Define what gets imported with "from simple_chatbot import *"
__all__ = [
    "chat",
    "get_conversation_history",
    "clear_history",
]
