import streamlit as st
from termcolor import colored
# from ydata_profiling import ProfileReport
import pycaret.regression as pycaret_base_reg
import pycaret.classification as pycaret_base_cls

from utils import get_model_info
from constants import MODELS_DICT, EXCLUDED_MODELS


def process_dataset_inner_function(pycaret_base, data, y):
    try:
        # profile_report = generate_profile_report(data)
        # print(YDATA_PROFILE_REPORT_TEXT, unsafe_allow_html=True)
            
        _ = pycaret_base.setup(data, target=y)
        environment_details_data = pycaret_base.pull()
 
        X_train_columns = pycaret_base.get_config("X_train").columns
        X_test = pycaret_base.get_config("X_test").head(1).values.tolist()
        
        best_model = pycaret_base.compare_models(exclude=EXCLUDED_MODELS)
        model_comparision_data = pycaret_base.pull()
            
        if best_model is not None:
            try:
                model_name = type(best_model).__name__
                print(f"Best model: {model_name}")
                
                model_id = MODELS_DICT.get(model_name, None)
                model_definition, model_info_links = get_model_info(model_name)

                if model_id is not None:
                    final_created_model = pycaret_base.create_model(model_id)
                    _ = pycaret_base.tune_model(final_created_model)
                    _ = pycaret_base.evaluate_model(final_created_model)
                    
                    model_evaluation_data = pycaret_base.pull()

                    serialized_model = {
                        "model_name": model_name,
                        "final_model": str(final_created_model),
                        "model_definition": model_definition,
                        "model_info_links": model_info_links,
                        "environment_details_data": str(environment_details_data),
                        "model_comparision_data": str(model_comparision_data),
                        "model_evaluation_data": str(model_evaluation_data),                      
                    }
                    
                    return serialized_model, best_model, X_train_columns

                else:
                    return "Woops, couldn't find a valid model for this one!"
            
            except Exception as e:
                return f"An error occurred while building and evaluating the best model: {str(e)}"
        
    except Exception as e:
        return f"An error occurred while finding the best model: {str(e)}"
    

def process_dataset(data, target, problem_type):
    try:
        pycaret_base = pycaret_base_cls if problem_type == 'classification' else pycaret_base_reg if problem_type in ['regression', 'classification'] else None
        print(f"Processing dataset for {problem_type}...")
        
        all_info, best_model, X_columns = process_dataset_inner_function(pycaret_base=pycaret_base,
                            data=data,
                            y=target
                        )
            
        return {"summary": all_info}, best_model, X_columns

    except Exception as e:
        return f"An error occurred while processing the dataset: {str(e)}"
    

def call_backend_api(uploaded_data_df, target_variable, problem_type):
    try:
        print(colored(f"Processing dataset for {problem_type}...", "green"))
        print(colored(f"target_variable variable: {target_variable}", "green"))

        if target_variable not in uploaded_data_df.columns:
            return {"error": f"target_variable column '{target_variable}' not found in the uploaded dataset!"}

        process_dataset_response, best_model, X_columns = process_dataset(uploaded_data_df, target_variable, problem_type)
        print(colored(process_dataset_response, "green"))
        
        return process_dataset_response, X_columns, pycaret_base_cls if problem_type == 'classification' else pycaret_base_reg if problem_type in ['regression', 'classification'] else None, best_model

    except Exception as e:
        return f"An error occurred: {e}", False, False, False
        
    
def display_response(response: dict) -> None:
    """
    Process the response from the api and display the results in a formatted manner.
    """
    data = response["summary"]
    try:
        model_name, final_model, model_definition, model_info_link = list(data.items())[:4]

        with st.expander("Model details", expanded=True):
            st.write(f"""
##### **Best model:** 
#### {model_name[1]}

###### **Parameters:** <br>
```
{final_model[1]}
```

##### **Description:** <br>
{model_definition[1]}

For more details, check out the following link:<br>
{model_info_link[1]}
            """, unsafe_allow_html=True)

        for keys, values in list(data.items())[-3:]:
            with st.expander(keys.replace("_", " ").title(), expanded=True):
                st.code(values)
        
    except Exception as e: 
        st.error(response)
    
if __name__ == "__main__":
    call_backend_api("misc/Iris.csv", "Species", "classification", ["Id"])