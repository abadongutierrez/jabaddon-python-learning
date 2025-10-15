from flask import Flask
from flask_cors import CORS
import json
import simple_chatbot
from flask import request

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/bananas')
def bananas():
    return 'Bananas are great!'

@app.route('/bread')
def bread():
    return 'I love bread!'

@app.route('/chatbot', methods=['POST'])
def handle_chatbot():
    # Read prompt from request
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data.get('prompt', '')

    simple_chatbot.chat(input_text)

    return json.dumps({
        'response': simple_chatbot.get_conversation_history()[-1] if simple_chatbot.get_conversation_history() else '',
        'conversation_history': simple_chatbot.get_conversation_history()
    }) 

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)