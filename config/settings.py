import os
from dotenv import load_dotenv, find_dotenv

load_dotenv("./env/.env")

TOKEN = os.environ.get("TOKEN")