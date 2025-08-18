import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-pro")  

def analyze_text(passage):
    response = model.generate_content(
        contents=[
            {"role": "user", "parts": [f"Analyze this passage deeply:\n\n{passage}"]}
        ]
    )
    return response.text

def what_if_generator(passage):
    response = model.generate_content(
        contents=[
            {"role": "user", "parts": [f"Create a dramatic 'what if' alternate version of this passage:\n\n{passage}"]}
        ]
    )
    return response.text