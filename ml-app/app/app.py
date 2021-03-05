from flask import Flask

from app.controller import pred_app

# factory functions
def create_app(config_object) -> Flask:
    """ Create a flask app instance """

    flask_app = Flask('ml_app')
    flask_app.config.from_object(config_object)

    flask_app.register_blueprint(pred_app)

    return flask_app


