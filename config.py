import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__name__), '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')