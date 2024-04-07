import streamlit as st
import google.generativeai as genai

GEMINI_INSTRUCTIONS = """
I am going to pass you a string. Your job is to write a single line pandas script to perform the task mentioned in the string. You can only use the pandas library. You have 2 minutes to complete the task.


"""


def parse_env_file(file_path):
    """
    Parse a .env file and return a dictionary of key-value pairs.
    """
    env_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                env_dict[key.strip()] = value.strip()
    return env_dict

# GOOGLE_API_KEY = parse_env_file('.env')["GOOGLE_API_KEY"]
# type(GOOGLE_API_KEY)
# genai.configure(api_key=GOOGLE_API_KEY)

def gemini_answers(question_string: str) -> str:
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question_string)
        return response.candidates[0].content.parts[0].text
    except Exception as e:  
        return f"An unexpected error occurred: {e}"
    
print(gemini_answers("Show me the top ten movies of all time."))