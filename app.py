import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Hello! Explain Artificial Intelligence in simple words."
)

print(response.text)