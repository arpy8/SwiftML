import streamlit as st
from pycaret.regression import *

try:
    from SwiftML.constants import MODELS_DICT
except ModuleNotFoundError:
    from constants import MODELS_DICT

INFO_COLOR = 'info'
SUCCESS_COLOR = 'success'

# loading_blocks = ("▒"*8, "█"*8)
block1 = "▒"*8
block2 = "█"*8

count1 = 8  
count2 = 0

def log_message(_temp_container, message, color):
    global block1, block2, count1, count2
    count2 += 1
    count1 -= 1
    
    perc = round((count2/8)*100)
    
    message_color = "red"
    
    if perc<50:
        message_color = "lightblue"
    elif perc<75:
        message_color = "lightyellow"
    elif perc<90:
        message_color = "lightgreen"
    else:
        message_color = "green"
    
    _temp_container.write(f"""
                            <b>{color.capitalize()}</b>: {message}
                            <br>
                            <center><span style='color:{message_color}'>{block2*count2}{block1*count1}</span>{"&nbsp;"*5}{perc}%</center>
                        """, unsafe_allow_html=True)

def setup_environment(_temp_container, data, y):
    log_message(_temp_container, "Setting up the environment for model comparison...", INFO_COLOR)
    setup(data, target=y)

def compare_and_get_best_model(_temp_container):
    global count1, count2
    log_message(_temp_container, "Comparing the models to find the best one...", INFO_COLOR)
    best_model = compare_models(n_select=1)
    log_message(_temp_container, f'Best model found: {type(best_model).__name__}', SUCCESS_COLOR)
    return best_model

def build_and_evaluate_best_model(_temp_container, best_model):
    global count1, count2
    model_name = type(best_model).__name__
    model_id = MODELS_DICT.get(model_name, None)

    if model_id is not None:
        log_message(_temp_container, "Best model found, building the best model...", INFO_COLOR)
        model = create_model(model_id)
        log_message(_temp_container, "Best model built successfully...", SUCCESS_COLOR)

        log_message(_temp_container, "Initiating model evaluation...", INFO_COLOR)
        evaluate_model(model)
        log_message(_temp_container, "Model evaluation completed successfully...", SUCCESS_COLOR)
        
        save_model_to_file(_temp_container, model, model_name)
        log_message(_temp_container, "Model saved successfully...", SUCCESS_COLOR)
        
        count1 = 8
        count2 = 0
        
        return model
    
    else:
        log_message(_temp_container, "Model ID not found in the mapping.", "error")
        
        count1 = 8
        count2 = 0
        
        return None

def save_model_to_file(_temp_container, model, model_name):
    save_model(model, "testmodel123")
    log_message(_temp_container, "Model saved successfully...", SUCCESS_COLOR)

def best_regressor(_temp_container, data, y, c1, c2):
    global count1, count2
    count1 = c1
    count2 = c2

    try:
        setup_environment(_temp_container, data, y)
        best_model = compare_and_get_best_model(_temp_container)

        if best_model is not None:
            return build_and_evaluate_best_model(_temp_container, best_model)
        else:
            return None

    except Exception as e:
        log_message(_temp_container, f"An error occurred: {str(e)}", "error")
        return None


if __name__ == "__main__":
    st = None
    your_data = None
    your_target_variable = None
    
    best_regressor(st, your_data, your_target_variable)