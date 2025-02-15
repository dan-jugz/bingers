from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__)
    # Setting up configuration
    app.config.from_object(DevConfig)
    app.config.from_pyfile('config.py')

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app