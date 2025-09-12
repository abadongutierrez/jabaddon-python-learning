from flask import Blueprint, jsonify

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