#code with API Endpoint

import openai
import requests

import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("openai.api_key")

URL = "https://api.openai.com/v1/chat/completions"

payload = {
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content": f"What is first computer in world? provide 1 line ans"}],
"temperature" : 1.0,
"top_p":1.0,
"n" : 1,
"stream": True,
"presence_penalty":0,
"frequency_penalty":0,
}

headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {openai.api_key}"
}

response = requests.post(URL, headers=headers, json=payload, stream=True)

response.content