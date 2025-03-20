import datetime
import os

from dotenv import load_dotenv
from flask import Config

load_dotenv()
APP_KEY = os.getenv("APP_KEY")

class DevelopConfig(Config):
    FLASK_DEBUG = True
    FLASK_ENV = "DEV"
    SECRET_KEY = APP_KEY
    SQLALCHEMY_RECORD_QUERIES = True

    SESSION_PERMANENT = datetime.timedelta(days=365)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///project.db"
    SESSION_USE_SIGNER = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = False
    SESSION_COOKIE_SAMESITE = 'Lax'