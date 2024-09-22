import google.generativeai as genai
import os
from dotenv import load_dotenv
import PIL.Image

# Load .env file
load_dotenv()

# get api key and invoke model
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

# saves chat history

def get_chat_response(chat: genai.ChatSession, prompt) -> str:
    text_response = []
    responses = chat.send_message(prompt, stream=True, tools=['code_execution'])
    for chunk in responses:
        text_response.append(chunk.text)
    return "".join(text_response)

def get_response_from_picture(picture_file, text):
    # if no picture is uploaded, only send in text
    if bool(picture_file) == False:
        return get_chat_response(chat, [text])
    else:
        file = PIL.Image.open(picture_file)
        return get_chat_response(chat, [text, file])
    

a = ''



