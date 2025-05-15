# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

DATABASE_URL = os.getenv("DATABASE_URL")
