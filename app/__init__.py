from flask import Flask
from config import config
from .main import main as main_blp


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.register_blueprint(main_blp)

    return app
