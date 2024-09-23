import google.generativeai as genai
import os
from dotenv import load_dotenv

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

def get_response_from_file(file, text):
    # if no picture is uploaded, only send in text
    if bool(file) == False:
        return get_chat_response(chat, [text])
    else:
        myFile = genai.upload_file(file)
        return get_chat_response(chat, [myFile, text])
