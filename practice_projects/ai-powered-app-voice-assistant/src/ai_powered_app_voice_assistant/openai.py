from openai import OpenAI
import os

openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Store conversation history (in-memory for this session)
conversation_history = []


def openai_process_message(user_message, conversation_history=None):
    """
    Process user message with conversation history support.

    Args:
        user_message: The user's message
        conversation_history: List of previous messages (optional)

    Returns:
        Tuple of (response_text, updated_conversation_history)
    """
    # Set the prompt for OpenAI Api
    system_prompt = "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations. Keep responses concise - 2 to 3 sentences maximum."

    # Initialize conversation history if not provided
    if conversation_history is None:
        conversation_history = []

    # Build messages array with system prompt and history
    messages = [{"role": "system", "content": system_prompt}]

    # Add conversation history (limit to last 10 messages to avoid token limits)
    messages.extend(conversation_history[-10:])

    # Add current user message
    messages.append({"role": "user", "content": user_message})

    # Call the OpenAI Api to process our prompt
    openai_response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=1000
    )
    print("openai response:", openai_response)

    # Parse the response to get the response message for our prompt
    response_text = openai_response.choices[0].message.content

    # Update conversation history with user message and assistant response
    updated_history = conversation_history.copy()
    updated_history.append({"role": "user", "content": user_message})
    updated_history.append({"role": "assistant", "content": response_text})

    return response_text, updated_history
