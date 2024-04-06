import time
import pickle
import wikipedia
import webbrowser
import streamlit as st
from ydata_profiling import ProfileReport
import pycaret.regression as pycaret_model_reg
import pycaret.classification as pycaret_model_cls

try:
    from SwiftML.__constants import EXCLUDED_MODELS, MODELS_DICT
    from SwiftML.__utils import path_convertor
except ModuleNotFoundError:
    from __constants import EXCLUDED_MODELS, MODELS_DICT

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

def build_and_evaluate_best_model(pycaret_model, best_model):
    try:
        model_name = type(best_model).__name__
        model_id = MODELS_DICT.get(model_name, None)
        
        if model_id is not None:
            with st.spinner("Training the best model ..."):
                model = pycaret_model.create_model(model_id)
                pycaret_model.tune_model(model)
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
                pycaret_model.evaluate_model(model)
            with st.expander("Evaluation details", expanded=True):
                st.code(pycaret_model.pull())
                
            # with st.spinner("Plotting the best model ..."):
            #     plot = pycaret_model.plot_model(model, plot="AUC", save=True)
            # with st.expander("Model plots", expanded=False):
            #     st.image("AUC.png")
                
            st.info("Model trained and evaluated successfully!, saving the model ...")
            save_model_locally(pycaret_model, model, model_name)
            st.info("Model saved successfully!")
            
            return model

        else:
            st.error("Woops, couldn't find a valid model for this one!")
    
    except Exception as e:
        st.error("An error occurred while building and evaluating the best model: " + str(e))
    
def save_model_locally(pycaret_model, model, model_name="model/test_model"):
    try:
        with st.spinner("Saving the best model ..."):
            pycaret_model.save_model(model, f"models/{model_name}")
            
            with open(f"models/dumped_{model_name}.pkl", "wb") as file:
                pickle.dump(model, file)
                
            st.info(f"Model saved successfully at `models/{model_name}`")

        st.success("Model saved successfully!")
        
    except Exception as e:
        st.error("An error occurred while saving the model: " + str(e))

def find_best_model(pycaret_model, data, y):
    try:
        with st.spinner("Generating Profile Report ..."):
                report_path = generate_profile_report(data)
        # st.toast("Profile Report generated successfully!")
        
        with st.expander("Profile Report details", expanded=False):
            st.write("Profile Report generated successfully!")
            st.write(f"A profile report has been generated for the dataset. Click [here]({report_path}) to view the report.")
            
        with st.spinner("Setting up the enviroment ..."):
            pycaret_model.setup(data, target=y)
        with st.expander("Environment details", expanded=False):
            st.code(pycaret_model.pull())

        with st.spinner("Comparing different models ..."):
            best_model = pycaret_model.compare_models(exclude=EXCLUDED_MODELS, budget_time = 0.5)
        with st.expander("Model Comparision", expanded=True):
            st.code(pycaret_model.pull())

        if best_model is not None:
                return build_and_evaluate_best_model(pycaret_model, best_model)
        return None

    except Exception as e:
        st.error("An error occurred while finding the best model: " + str(e))

def process_dataset(data, target, query):
    try:
        pycaret_model = pycaret_model_cls if query=="cls" else pycaret_model_reg

        start_time = time.time()
        _ = find_best_model(pycaret_model=pycaret_model,
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