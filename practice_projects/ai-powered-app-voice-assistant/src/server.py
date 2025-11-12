from flask import Flask, request, render_template, jsonify
import json
import base64
import os
from pathlib import Path
from worker import speech_to_text, text_to_speech, openai_process_message

# Get the project root directory (parent of src/)
project_root = Path(__file__).parent.parent

app = Flask(__name__,
            template_folder=str(project_root / 'templates'),
            static_folder=str(project_root / 'static'))

# In-memory conversation history (will be lost when app restarts)
conversation_history = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    print("processing speech-to-text")
    audio_binary = request.data # Get the user's speech from their request
    text = speech_to_text(audio_binary) # Call speech_to_text function to transcribe the speech

    # Return the response back to the user in JSON format
    response = app.response_class(
        response=json.dumps({'text': text}),
        status=200,
        mimetype='application/json'
    )
    print(response)
    print(response.data)
    return response

@app.route('/process-message', methods=['POST'])
def process_message_route():
    global conversation_history

    user_message = request.json['userMessage'] # Get user's message from their request
    print('user_message', user_message)

    voice = request.json['voice'] # Get user's preferred voice from their request
    print('voice', voice)

    # Call openai_process_message function with conversation history
    print(f'Current conversation history length: {len(conversation_history)}')
    openai_response_text, conversation_history = openai_process_message(user_message, conversation_history)
    print(f'Updated conversation history length: {len(conversation_history)}')

    # Clean the response to remove any emptylines
    openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])

    # Call our text_to_speech function to convert OpenAI Api's reponse to speech
    openai_response_speech = text_to_speech(openai_response_text, voice)

    # convert openai_response_speech to base64 string so it can be sent back in the JSON response
    openai_response_speech = base64.b64encode(openai_response_speech).decode('utf-8')

    # Send a JSON response back to the user containing their message's response both in text and speech formats
    response = app.response_class(
        response=json.dumps({"openaiResponseText": openai_response_text, "openaiResponseSpeech": openai_response_speech}),
        status=200,
        mimetype='application/json'
    )

    print(response)
    return response


@app.route('/clear-history', methods=['POST'])
def clear_history_route():
    """Clear the conversation history"""
    global conversation_history
    conversation_history = []
    return jsonify({"status": "success", "message": "Conversation history cleared"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
