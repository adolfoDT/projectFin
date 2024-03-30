from .routes import main

from flask import Flask
from redis import Redis

def create_app():
    app = Flask(__name__)
    app.redis = Redis(host='redis', port=6379)

    app.register_blueprint(main)

    return app
