import openai
import gradio
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("openai.api_key")

messages = [{"role": "system", "content": "You are a dictionary, provide meaning when a word is prompted"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Greeshma's First Dictionary :v4")

demo.launch(share=True)