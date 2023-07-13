import os
import openai
openai.api_key = os.getenv("openai.api_key")
openai.Model.list()
