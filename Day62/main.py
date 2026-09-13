import os
from dotenv import load_dotenv

load_dotenv()

name = os.environ.get("MY_NAME")

print(name)