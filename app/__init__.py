from flask import Flask
from app.extensions import db, bcrypt, jwt, ma, swagger
from app.resources import create_resources
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    swagger.init_app(app)

    # Register resources
    create_resources(app)

    return app
