from dotenv import load_dotenv
from flask import Flask, session, redirect, flash, url_for
from App.config import DevelopConfig
from App.extensions import db
from App.app import my_app
from Models.User import User
from faker import Faker
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopConfig)
    db.init_app(app)


    with app.app_context():
        db.drop_all()
        db.create_all()

    app.register_blueprint(my_app)
    return app