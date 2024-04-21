import json
import requests
import streamlit as st

# API_ENDPOINT = 'https://swiftml-backend.onrender.com/upload/'
API_ENDPOINT = 'http://localhost:8000/upload/'

def call_backend_api(target, problem_type):
    uploaded_file = 'temp_data.csv'
    print(target, problem_type)
    
    form_data = {
        'target_variable': target,
        'problem_type': problem_type,
    }

    files = {'file': open(uploaded_file, 'rb')}

    # try:  
    print("process started")
    response = requests.post(API_ENDPOINT, files=files, data=form_data)
    print("process finished")
    print("response", response.text)

    if response.status_code == 200:
        return json.loads(response.text)
    
    else:
        return f"Failed to upload file. Status code: {response.status_code}" 

    # except Exception as e:
    #     return f"An error occurred: {e}"
        
    
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
    
    st.toast(f"Process finished in {round(float(response['elapsed_time']), 2)} seconds.", icon="✅")
    
if __name__ == "__main__":
    call_backend_api("misc/Iris.csv", "Species", "classification", ["Id"])