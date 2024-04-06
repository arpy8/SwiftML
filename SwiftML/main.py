import os
import tqdm
import time
import random
import subprocess
from datetime import datetime
from termcolor import colored

try:
    from SwiftML.__utils import path_convertor
    from SwiftML.__constants import ART, PORT
except ModuleNotFoundError:
    from __utils import path_convertor
    from __constants import ART, PORT


def boot_sequence():
    for _ in tqdm.tqdm(range(10), desc="Initializing boot sequence..."):
        time.sleep(random.uniform(0.08, 0.12))

    print(f"{colored('Boot sequence initialized.', 'green')}\nLoading modules...")
    
    time.sleep(1)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(chr(27)+'[2j')
    curr_time = datetime.now().strftime("%H:%M:%S")
    print(f"{colored(ART, 'green')}\n{colored(f'[{curr_time}] App started, http://localhost:{PORT}/', 'blue')}")

def run_streamlit_app(PORT):
    exe_path = path_convertor('__streamlit_app.py')
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