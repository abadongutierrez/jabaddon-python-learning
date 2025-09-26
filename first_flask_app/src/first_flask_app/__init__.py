import os
from flask import Flask, jsonify
from .config import config_by_name
from .routes.main import main
from .routes.health import health
from .routes.courses import course
from .routes.todo import todo_bp

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app = Flask(__name__, template_folder='../../templates')
    app.config.from_object(config_by_name[config_name])
    
    app.register_blueprint(main)
    app.register_blueprint(health)
    app.register_blueprint(course)
    app.register_blueprint(todo_bp)
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    @app.errorhandler(Exception)
    def unhandled_exception(e):
        return jsonify({'error': str(e)}), 500

    @app.before_request
    def before_request():
        # You can add code here to run before each request
        pass

    @app.after_request
    def after_request(response):
        # You can add code here to run after each request
        return response

    return app