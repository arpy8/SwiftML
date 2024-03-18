import os
import pkg_resources
from termcolor import colored
from datetime import datetime

def stop_streamlit_app():
    print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] App stopped successfully", "red"))
    os.system('taskkill /f /im "streamlit.exe"')
    
def path_converter(filename):
    return pkg_resources.resource_filename('SwiftML', f'{filename}')