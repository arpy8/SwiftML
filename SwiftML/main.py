import os
import tqdm
import time
import random
import subprocess
from datetime import datetime
from termcolor import colored

try:
    from SwiftML.utils import path_converter
    from SwiftML.constants import ART, PORT
except ModuleNotFoundError:
    from utils import path_converter
    from constants import ART, PORT
    

def boot_sequence():
    for _ in tqdm.tqdm(range(10), desc="Initializing boot sequence..."):
        time.sleep(random.uniform(0.08, 0.12))

    print(f"{colored('Boot sequence initialized.', 'green')}\nLoading modules...")
    
    time.sleep(1)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(chr(27)+'[2j')
    print(f"{colored(ART, 'green')}\n{colored(f"[{datetime.now().strftime('%H:%M:%S')}] App started, http://localhost:{PORT}/", "blue")}")

def run_streamlit_app(PORT):
    exe_path = path_converter('streamlit_app.py')
    command = ['streamlit', 'run' , exe_path, '--server.port', f'{PORT}']
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    return result.stdout

def main():
    try:
        boot_sequence()
        run_streamlit_app(PORT)
    except KeyboardInterrupt:
        print(colored("Bye Bye 🤫🧏...", "red"))
        exit()
    except Exception as e:
        print(e)
        print(colored("Exiting...", "red"))
        exit()
        
if __name__ == '__main__':
    main()