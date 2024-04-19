import time
import pickle
import webbrowser
import streamlit as st
from ydata_profiling import ProfileReport
import pycaret.regression as pycaret_base_reg
import pycaret.classification as pycaret_base_cls

# try:
# from SwiftML.__constants import EXCLUDED_MODELS, MODELS_DICT, README_TEXT_CONTENT
# from SwiftML.__utils import path_convertor, generate_sha256, get_model_folder
# except ModuleNotFoundError:

from __utils import generate_sha256, get_model_folder, get_model_info
from __constants import EXCLUDED_MODELS, MODELS_DICT, README_TEXT_CONTENT, YDATA_PROFILE_REPORT_TEXT, PREDICTION_SCRIPT, ENCODING_IMPORTANT, PREDICT_FASTAPI_SCRIPT, API_REQUIREMENTS, API_README

pr = None
profile_report = ""
uploaded_csv_name = None


def generate_profile_report(data):
    global pr
    
    pr = ProfileReport(data, title='Profile Report')
    return pr

def create_model_api(pycare_base, model, api_path):
    return pycare_base.create_api(model, api_path)

def save_model_locally(pycaret_base, params, model, X_test):
    try:
        with st.spinner("Saving the files ..."):
            sha256_string = generate_sha256()
            documents_dir = get_model_folder(uploaded_csv_name, model_name)
            pickle_content = [params, model]

            sha_model_name = f"{sha256_string}.pkl"

            report_path = f"{documents_dir}/profile-report.html"
            readme_path = f"{documents_dir}/README.txt"
            model_path = f"{documents_dir}/{sha_model_name}"
            predict_path = f"{documents_dir}/predict.py"

            #### api dir
            api_dir = f"{documents_dir}/api"
            
            fastapi_script_path = f"{api_dir}/app.py"
            fastapi_script_path2 = f"{api_dir}/app_pycaret"
            
            reqs_path = f"{api_dir}/requirements.txt"
            api_readme_path = f"{api_dir}/README.txt"
            
            profile_report.to_file(report_path)
            webbrowser.open(report_path)
            
            with open(model_path, "wb") as file:
                pickle.dump(pickle_content, file)
                
            with open(readme_path, "wb") as file:
                content = README_TEXT_CONTENT.format(sha256_string=sha256_string, params=params)
                file.write(content.encode())
                
            with open(predict_path, "w") as file:
                content = PREDICTION_SCRIPT.format(values=X_test, model_path=f"{documents_dir}/{sha_model_name}")
                file.write(content)

            # populating api dir
            with open(f"{api_dir}/{sha_model_name}", "wb") as file:
                pickle.dump(pickle_content, file)
                
            with open(fastapi_script_path, "w") as file:
                content = PREDICT_FASTAPI_SCRIPT.format(model_path=sha_model_name, result_dict='{"prediction": prediction, "model": model.__class__.__name__}')
                file.write(content)
                
            with open(reqs_path, "w") as file:
                file.write(API_REQUIREMENTS)

            with open(api_readme_path, "w") as file:
                file.write(API_README)
                

            if any(isinstance(i, str) for i in X_test[0]):
                st.warning("Please note that the feature variables contains categorical values. Make sure to encode these values before making predictions. For more information, check the `IMPORTANT.md` file.")
                
                with open(f"{documents_dir}/IMPORTANT.md", "w") as file:
                    file.write(ENCODING_IMPORTANT)
                
        st.success(f"""
                    Model files saved successfully at:

                    `{documents_dir}`
                """)

        _ = create_model_api(pycaret_base, model, fastapi_script_path2)
        
        return model_path
        
    except Exception as e:
        st.error("An error occurred while saving the model: " + str(e))

def build_and_evaluate_best_model(pycaret_base, params, best_model, X_test):
        global model_name
    
    # try:
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
            
            _ = save_model_locally(pycaret_base, params, model, X_test)
            
            return model

        else:
            st.error("Woops, couldn't find a valid model for this one!")
    
    # except Exception as e:
        # st.error("An error occurred while building and evaluating the best model: " + str(e))
    
def find_best_model(pycaret_base, data, y):
    global profile_report
    
    try:
        with st.spinner("Generating Profile Report ..."):
            profile_report = generate_profile_report(data)
        
        with st.expander("Profile Report details", expanded=False):
            st.write(YDATA_PROFILE_REPORT_TEXT, unsafe_allow_html=True)
            st.caption("Generated with the help of")
            st.image("https://assets.ydata.ai/oss/ydata-profiling_red.png", width=70, )
            
        with st.spinner("Setting up the enviroment ..."):
            pycaret_base.setup(data, target=y)
            params = pycaret_base.get_config("X_train").columns
            X_test = pycaret_base.get_config("X_test").head(1).values.tolist()
        
        with st.expander("Environment details", expanded=True):
            st.code(pycaret_base.pull())

        with st.spinner("Comparing different models ..."):
            best_model = pycaret_base.compare_models(exclude=EXCLUDED_MODELS)
        with st.expander("Model Comparision", expanded=True):
            st.code(pycaret_base.pull())
            
        if best_model is not None:
            return build_and_evaluate_best_model(pycaret_base, params, best_model, X_test)

        return None

    except Exception as e:
        st.error("An error occurred while finding the best model: " + str(e))

def process_dataset(data, target, query, uploaded_file_name):
    
    global uploaded_csv_name
    uploaded_csv_name = uploaded_file_name
    
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