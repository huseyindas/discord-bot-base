import os
import logging
from dotenv import load_dotenv, find_dotenv

load_dotenv("./env/.env")

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
    # It will remain as a comment line during development.
    # filename='bot.log',
    # encoding='utf-8'
    )

TOKEN = os.environ.get("TOKEN")
PREFIX = os.environ.get("PREFIX")