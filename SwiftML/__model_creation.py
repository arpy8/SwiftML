import time
import pickle
import wikipedia
import webbrowser
import streamlit as st
from ydata_profiling import ProfileReport
import pycaret.regression as pycaret_base_reg
import pycaret.classification as pycaret_base_cls

# try:
#     from SwiftML.__constants import EXCLUDED_MODELS, MODELS_DICT
#     from SwiftML.__utils import path_convertor
# except ModuleNotFoundError:

from __utils import path_convertor
from __constants import EXCLUDED_MODELS, MODELS_DICT, YDATA_PROFILE_REPORT_TEXT

def generate_profile_report(data):
    report_path = path_convertor('profile-report.html')
    pr = ProfileReport(data, title='Profile Report')   
    pr.to_file(report_path)
    
    webbrowser.open(report_path)
    return report_path

def get_model_info(model_name):
    try:
        description = wikipedia.summary(model_name, sentences=4)
        link = wikipedia.page(model_name).url
        return description, link
    except wikipedia.exceptions.PageError:
        print(f"No Wikipedia page found for '{model_name}'")
        return "No description found!", "No link found!"


def save_model_locally(params, model, model_name="model/test_model"):
    try:
        with st.spinner("Saving the best model ..."):
            pickle_content = [params, model]
            file_name = f"models/final_dumped_{model_name}.pkl"
            
            with open(file_name, "wb") as file:
                pickle.dump(pickle_content, file)
                
            st.success(f"Model saved successfully at : {file_name}")
        
    except Exception as e:
        st.error("An error occurred while saving the model: " + str(e))

def build_and_evaluate_best_model(pycaret_base, params, best_model):
    try:
        model_name = type(best_model).__name__
        model_id = MODELS_DICT.get(model_name, None)

        if model_id is not None:
            with st.spinner("Training the best model ..."):
                model = pycaret_base.create_model(model_id)
                pycaret_base.tune_model(model)
                model_def, link = get_model_info(model_name)
            with st.expander("Model details", expanded=True):
                st.write(f"""
Best model: `{model_name}`

```
{best_model}
```

**Description:**
{model_def}

For more details, check out the following link:<br>
{link}
                """, unsafe_allow_html=True)
                
            with st.spinner("Evaluating the best model ..."):
                pycaret_base.evaluate_model(model)
            with st.expander("Evaluation details", expanded=True):
                st.code(pycaret_base.pull())
                
            # with st.spinner("Plotting the best model ..."):
            #     plot = pycaret_base.plot_model(model, plot="AUC", save=True)
            # with st.expander("Model plots", expanded=False):
            #     st.image("AUC.png")
            
            save_model_locally(params, model, model_name)
            return model

        else:
            st.error("Woops, couldn't find a valid model for this one!")
    
    except Exception as e:
        st.error("An error occurred while building and evaluating the best model: " + str(e))
    
def find_best_model(pycaret_base, data, y):
    try:
        with st.spinner("Generating Profile Report ..."):
            report_path = generate_profile_report(data)
            st.toast("Profile Report generated successfully!")
        
        with st.expander("Profile Report details", expanded=False):
            st.write(YDATA_PROFILE_REPORT_TEXT.format(report_path=report_path), unsafe_allow_html=True)
            st.caption("Generated with the help of")
            st.image("https://assets.ydata.ai/oss/ydata-profiling_red.png", width=70, )
            
        with st.spinner("Setting up the enviroment ..."):
            pycaret_base.setup(data, target=y)
            params = pycaret_base.get_config("X_train").columns
        
        with st.expander("Environment details", expanded=False):
            st.code(pycaret_base.pull())

        with st.spinner("Comparing different models ..."):
            best_model = pycaret_base.compare_models(exclude=EXCLUDED_MODELS)
        with st.expander("Model Comparision", expanded=True):
            st.code(pycaret_base.pull())
            
        if best_model is not None:  
            return build_and_evaluate_best_model(pycaret_base, params, best_model)

        return None

    except Exception as e:
        st.error("An error occurred while finding the best model: " + str(e))

def process_dataset(data, target, query):
    try:
        pycaret_base = pycaret_base_cls if query == 'Classification' else pycaret_base_reg if query in ['Regression', 'Classification'] else None
        start_time = time.time()
        
        _ = find_best_model(pycaret_base=pycaret_base,
                            data=data,
                            y=target
                        )
        end_time = time.time()
        elapsed_time = end_time - start_time
        st.toast("Process completed in {} seconds.".format(round(elapsed_time, 2)))

    except KeyboardInterrupt:
        st.error("Process interrupted by the user!")

    except Exception as e:
        st.write(e)
            
if __name__ == "__main__":
    data_path = r"SwiftML\assets\dataset\Iris.csv"
    target = "Species"
    problem_type = "cls"
    
    process_dataset(data_path, target, problem_type)