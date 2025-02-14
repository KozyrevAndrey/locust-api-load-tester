import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent.parent
dotenv_path = os.path.join(BASE_DIR, ".env")

ENDPOINTS = {
    "pinata_init": "/api/pinata/init/",
}
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

env = os.environ


BASE_URL = "http://localhost:8000"

API_KEY = env.get("API_KEY")

print(BASE_DIR)
print(API_KEY)
