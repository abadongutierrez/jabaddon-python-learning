from flask import Blueprint, jsonify, request

health = Blueprint('health', __name__)

@health.route('/health')
def health_check():
    if request.method == 'GET':
        return jsonify({'status': 'OK', 'server': request.server}), 200
    if request.method == 'POST':
        return jsonify({'status': 'Created'}), 201
    return jsonify({'error': 'Method not allowed'}), 405