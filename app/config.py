import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent
dotenv_path = os.path.join(BASE_DIR, ".env")


if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

env = os.environ


BASE_URL = "http://localhost:8000"

API_KEY = env.get("API_KEY")


ENDPOINTS = {
    # Add your API endpoints here
    "dummy": "/api/dummy/",
}
