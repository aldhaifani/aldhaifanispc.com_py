from flask import Flask
import os


def create_app():
    """Creates the flask app

    Return:
        the flask app
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(24)

    return app
