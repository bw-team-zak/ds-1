# web_app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask
from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
#from web_app.routes.test_routes import test_routes (might delete)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    #app.register_blueprint(test_routes)(might delete)
    return app