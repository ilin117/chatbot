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

# def get_response(user_input: str):
#     try:
#         response = model.generate_content(user_input)
#     except UnboundLocalError and TypeError:
#         response = model.generate_content("Say 'Say something to me!'")
#     return response.text

def get_response_from_picture(picture_file, text):
    file = PIL.Image.open(picture_file)
    result = model.generate_content([text, file], tools=['code_execution'])
    return result.text

