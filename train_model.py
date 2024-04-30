import pandas as pd
import streamlit as st
# from ydata_profiling import ProfileReport
import pycaret.regression as pycaret_base_reg
import pycaret.classification as pycaret_base_cls

from utils import get_model_info
from constants import MODELS_DICT, EXCLUDED_MODELS, MODEL_DETAILS_TEMPLATE



def process_dataset(data:pd.core.frame.DataFrame, target:str, problem_type:str) -> bool:
    """
    This function processes the uploaded dataset to determine the best model for the given problem.
    
    Parameters:
        data (pd.core.frame.DataFrame): The dataset to be processed.
        target (str): The target variable or column in the dataset.
        problem_type (str): The type of problem, whether it's regression or classification.

    Returns:
        bool: True if the processing is successful, False otherwise.

    Description:
        This function takes a pandas DataFrame containing the dataset, the name of the target variable, and the type of problem to be solved (regression or classification).
        It then performs data preprocessing, feature engineering, and model selection to find the most suitable model for the given dataset.
        The function stores various details such as environment information, model comparison data, model evaluation data, and the final selected model in the session state.
        Finally, it returns True if the processing is successful, indicating that the best model has been determined and stored in the session state, or False if an error occurs during processing.
    """

    if target not in data.columns:  
        return {"Error": f"target_variable column '{target}' not found in the uploaded dataset!"}
    
    try:
        st.session_state['data'] = data
        
        pycaret_base = {
            'classification': pycaret_base_cls,
            'regression': pycaret_base_reg
        }
        pycaret_base = pycaret_base[problem_type]
        st.session_state['pycaret_base'] = pycaret_base
        
        pycaret_base.setup(data=data, target=target)
        environment_details_data = pycaret_base.pull()
        st.session_state['environment_details_data'] = str(environment_details_data)
 
        X_train_columns = pycaret_base.get_config("X_train").columns
        X_test = pycaret_base.get_config("X_test").head(1).values.tolist()
        st.session_state['X_train_columns'], st.session_state['X_test'] = X_train_columns, X_test
        
        best_model = pycaret_base.compare_models(exclude=EXCLUDED_MODELS)
        model_comparision_data = pycaret_base.pull()
        st.session_state['model_comparision_data'] = str(model_comparision_data)
            
        model_name = type(best_model).__name__
        st.session_state['model_name'] = model_name
        
        model_id = MODELS_DICT.get(model_name, None)
        model_definition, model_info_link = get_model_info(model_name)
        st.session_state['model_definition'], st.session_state['model_info_link'] = model_definition, model_info_link

        final_model = pycaret_base.create_model(model_id)
        pycaret_base.tune_model(final_model)
        pycaret_base.evaluate_model(final_model)
        st.session_state['final_model'] = final_model

        model_evaluation_data = pycaret_base.pull()
        st.session_state['model_evaluation_data'] = str(model_evaluation_data)

        return True
        
    except Exception:
        return False

def display_response() -> None:
    """
    This function displays the response generated from the processing function.

    Parameters:
        None

    Returns:
        None

    Description:
        This function is responsible for displaying the response generated from the processing function.
        It retrieves the stored response from the session state, which includes information such as model comparison data, evaluation metrics, and the final selected model.
        The response is then formatted and presented to the user for interpretation.
        If there is no stored response or if an error occurs while retrieving it, an appropriate message is displayed to notify the user.
    """
    
    model_name = st.session_state["model_name"]
    final_model = st.session_state["final_model"]
    model_definition = st.session_state["model_definition"]
    model_info_link = st.session_state["model_info_link"]
    
    try:
        with st.expander("Model details", expanded=True):
            st.write(MODEL_DETAILS_TEMPLATE.format(
                    model_name=model_name, final_model=str(final_model), model_definition=model_definition, model_info_link=model_info_link
            ), unsafe_allow_html=True)

        for key in sorted([i for i in st.session_state.keys() if "_data" in i]):
            with st.expander(key.replace("_", " ").title(), expanded=True):
                st.code(st.session_state[key])
        
    except Exception as e: 
        st.error(f"An error occurred while displaying the model details: {str(e)}")

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("misc/Iris.csv")
    df = pd.DataFrame(df)
    
    with st.spinner():
        response = process_dataset(df, "Species", "classification")
    
    st.write(st.session_state)