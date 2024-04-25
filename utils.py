import wikipedia
from constants import MODEL_NAME_INFO
    
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