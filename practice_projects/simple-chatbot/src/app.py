from flask import Flask, render_template
from flask_cors import CORS
import json
import simple_chatbot
from flask import request
import os

# Get the directory of this file
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
            template_folder=os.path.join(basedir, 'templates'),
            static_folder=os.path.join(basedir, 'static'))
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

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

    # Get response from chatbot
    response = simple_chatbot.chat(input_text)

    return json.dumps({
        'response': response if response else '',
        'conversation_history': simple_chatbot.get_conversation_history()
    }) 

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)