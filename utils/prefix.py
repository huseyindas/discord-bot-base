import os
import logging
from posix import environ
import dotenv

dotenv_file = dotenv.find_dotenv("./env/.env")
dotenv.load_dotenv(dotenv_file)

def ChangePrefix(prefix):
    if len(prefix) < 4:
        os.environ["PREFIX"] = str(prefix)
        dotenv.set_key(dotenv_file, "PREFIX", os.environ["PREFIX"])
        return True




# dotenv_file = dotenv.find_dotenv()
# dotenv.load_dotenv(dotenv_file)

# print(os.environ["key"])  # outputs "value"
# os.environ["key"] = "newvalue"
# print(os.environ['key'])  # outputs 'newvalue'

# # Write changes to .env file.
# dotenv.set_key(dotenv_file, "key", os.environ["key"])