import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__name__), '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or f'{os.path.join(os.path.dirname(__file__), "app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
