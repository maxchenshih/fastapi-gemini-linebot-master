from api.prompt import Prompt
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("AIzaSyDFZf0C_bKk0W8xij8uldAS-l2Bmc_8Jl0"))

class Gemini:
    def __init__(self):
        self.prompt = Prompt()
        self.model = genai.GenerativeModel('gemini-pro')

    def get_response(self):
        tmp = self.prompt.generate_prompt()
        response = self.model.generate_content(tmp)
        return response.text
    
    def add_msg(self, text):
        self.prompt.add_msg(text)
