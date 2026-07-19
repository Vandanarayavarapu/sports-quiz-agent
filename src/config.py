import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Read Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("Warning: Gemini API Key not found!")