# web_app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask
from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    return app