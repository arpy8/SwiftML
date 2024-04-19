import os
import string
import random
import hashlib
import wikipedia
import pkg_resources
from termcolor import colored
from datetime import datetime

try:
    from SwiftML.__constants import MODEL_NAME_INFO
except ImportError:
    from constants import MODEL_NAME_INFO
    

def stop_streamlit_app():
    print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] App stopped successfully", "red"))
    os.system('taskkill /f /im "streamlit.exe"')
    
def path_convertor(filename):
    return pkg_resources.resource_filename('SwiftML', f'{filename}')

def generate_sha256():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
    result = hashlib.sha256(result_str.encode())
    return result.hexdigest()

def get_model_folder(csv_file_name, model_name):
    doc_folder = os.path.expanduser(r"~\Documents")
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H%M%S")
    
    swiftml_folder = os.path.join(doc_folder, "SwiftML")
    date_folder = os.path.join(swiftml_folder, date)
    custom_folder = os.path.join(date_folder, f"{time}_{csv_file_name.split('.')[0]}_{model_name}")
    api_folder = os.path.join(custom_folder, "api")
    
    if not os.path.exists(swiftml_folder):
        os.makedirs(swiftml_folder)
    if not os.path.exists(date_folder):
        os.makedirs(date_folder)
    if not os.path.exists(custom_folder):
        os.makedirs(custom_folder)
    if not os.path.exists(api_folder):
        os.makedirs(api_folder)
    
    return os.path.join(doc_folder, "SwiftML", date, custom_folder).replace("\\", "/")

def get_model_info(model_name):
    try:
        if model_name in MODEL_NAME_INFO:
            return MODEL_NAME_INFO[model_name][0], MODEL_NAME_INFO[model_name][1] 
        
        description = wikipedia.summary(model_name, sentences=4)
        link = wikipedia.page(model_name).url
        return description, link
    
    
    except ConnectionError:
        return "Couldn't fetch data due to connection error!", "No link found!"
        
    except wikipedia.exceptions.PageError:
        print(f"No Wikipedia page found for '{model_name}'")
        return "No description found!", "No link found!"