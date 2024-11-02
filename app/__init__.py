from flask import Flask
from config import config
import pymongo
from flask import Flask
from .database import Database


# App initialization with MongoClient
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize the database with the MongoDB URI
    Database.initialize(app.config['MONGO_URI'])

    # Routes (Blueprints)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app