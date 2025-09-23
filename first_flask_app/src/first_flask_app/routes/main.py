from flask import Blueprint, jsonify, render_template

main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return 'Hello World!'

@main.route('/json')
def hello_world_json():
    return {'message': 'Hello, World!'}

@main.route('/jsonify')
def hello_world_jsonify():
    return jsonify({'message': 'Hello, World!'})

@main.route('/sample')
def sample():
    return render_template('sample.html', title='Sample Page', message='This is a sample page rendered with a template.')