from dotenv import load_dotenv
from flask import Flask, session, redirect, flash, url_for
from .config import DevelopConfig
from App.extensions import db
from .app import my_app
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopConfig)

    db.init_app(app)
    app.register_blueprint(my_app)
    return app