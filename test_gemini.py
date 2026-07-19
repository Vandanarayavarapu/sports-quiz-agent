import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send a test message
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say Hello! My AI Sports Quiz project is working."
)

print(response.text)