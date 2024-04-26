import os
import time
import base64
import pandas as pd
import streamlit as st
from st_on_hover_tabs import on_hover_tabs

from constants import BACKGROUND, PAGE_ICON
from train_model import call_backend_api, display_response


st.set_page_config(page_title='SwiftML', page_icon=PAGE_ICON, layout='wide')

if 'disable_button' not in st.session_state:
    st.session_state['disable_button'] = False

def set_page_background(png_file):
    @st.cache_data()
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
        <style>
        {header_css}
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            }}
        </style>
    '''.format(
        header_css=open('assets/css/styles.css').read(),
        bin_str=bin_str
    )
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_page_background(BACKGROUND)

with st.columns([3,3,1])[2]:
    st.write(open('assets/html_components/logo.html', 'r').read(), unsafe_allow_html=True)

with st.sidebar:
    st.write('<br>', unsafe_allow_html=True)
    selected_task = on_hover_tabs(
        tabName=['Home Page', 'Process Dataset', 'Predict Values', 'Download Model', 'Learn ML', 'About Us'],
        iconName=['home', 'engineering', 'lightbulb', 'download', 'school', 'contact_support'],
        styles = {
            'navtab': {'background-color':'#ffffff',
                        'color': '#ff0290',
                        'padding': '40px 0px 10px 0px',
                        'border-radius': '23px',
                        'font-size': '18px',
                        'transition': '.5s',
                        'white-space': 'nowrap',
                        'text-transform': 'uppercase',
            },
            'tabOptionsStyle': {':hover :hover': {'color': '#170034',
                                            'cursor': 'pointer'},
                            },
            'iconStyle':{'position':'fixed',
                        'left':'11.5px'},
            'tabStyle' : {'background-color':'rgba(0, 0, 0, 0)',
                        'list-style-type': 'none',
                        'margin-bottom': '30px',
                        },
            },
        key="1",
        default_choice=1)

if selected_task == 'Home Page':
    st.write(open('assets/html_components/home.html', 'r').read(), unsafe_allow_html=True)

elif selected_task == 'Process Dataset':
    header_container = st.empty()
    header_container.write("""
            <div style='text-align:center;'>
                <h1 style='text-align:center; font-size: 300%;'>Process Dataset</h1>
                <p style=' color: #9c9d9f'>Upload your dataset and watch us do the magic.</p>
                <hr>
            </div>
             """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader('Please upload a dataset', type=['csv'])
    # uploaded_file = r'misc\Iris.csv'
    dataset_option_columns = st.columns([2,2,3,1])
    
    if uploaded_file is not None:
        uploaded_data_df = pd.read_csv(uploaded_file)
        
        with st.expander("Preview Data", expanded=False):
            with st.columns([1,100,1])[1]:
                uploaded_data_container = st.empty()
                    
        with dataset_option_columns[0]:
            st.write("##### Select Target Column")
            target = st.selectbox(
                                label='Select Target Column', 
                                options=uploaded_data_df.columns[::-1], 
                                label_visibility="hidden", 
                                disabled=st.session_state['disable_button']
                            )
        
        with dataset_option_columns[1]:
            st.write("##### Select Target Type")
            problem_type = st.selectbox(
                                label='Select Target Type', 
                                options=["Regression", "Classification"], 
                                label_visibility="hidden", 
                                disabled=st.session_state['disable_button']
                            )
        
        with dataset_option_columns[2]:
            st.write("##### Select Extra Columns")
            metadata_columns = st.multiselect(
                                    label='Select Extra Columns', 
                                    options=[i for i in uploaded_data_df.columns if i!=target], 
                                    label_visibility="hidden",
                                    disabled=st.session_state['disable_button'], 
                                    placeholder="Select extra columns to drop"
                                )
            trimmed_uploaded_data = uploaded_data_df[[column for column in uploaded_data_df.columns if column not in metadata_columns]]
            

        with dataset_option_columns[3]:
            st.write("<br><br>", unsafe_allow_html=True)
            submit_uploaded_file_container = st.empty()
            
        _ = uploaded_data_container.dataframe(trimmed_uploaded_data, hide_index=True, width=2000)
        
        if submit_uploaded_file_container.button(label='Submit', use_container_width=True):
            _ = header_container.empty()
            _ = submit_uploaded_file_container.empty()
            
            st.write("---")
            
            start_time = time.time()
            
            try:
                with st.spinner("Processing data..."):
                    api_response, X_columns, pycaret_instance, best_model  = call_backend_api(trimmed_uploaded_data, target, problem_type.lower())
                
                if type(api_response) == dict:
                    try:    
                        if 'data' not in st.session_state:
                            st.session_state['trimmed_uploaded_data'] = trimmed_uploaded_data
                        if 'model_info' not in st.session_state:
                            st.session_state['model_info'] = api_response
                            
                        _ = display_response(api_response)
                        
                        if 'pycaret_instance' not in st.session_state:
                            st.session_state['pycaret_instance'] = pycaret_instance
                        if 'X_df' not in st.session_state:
                            st.session_state['X_df'] = X_columns
                            
                        if 'best_model' not in st.session_state:
                            st.toast('Model trained successfully!', icon='✅')
                            st.session_state['best_model'] = best_model

                    except KeyError:
                        st.error(f'An error occurred while processing the dataset: {api_response}')
                else:
                    st.error(api_response)
                
                _ = submit_uploaded_file_container.button(label='Submit', use_container_width=True, key='submit_button2')

            except UnicodeDecodeError:
                st.error('Error reading file: UnicodeDecodeError')
                
            end_time = time.time()
            st.toast(f"Processed finished in : {end_time-start_time:.2f} seconds.")

    else:
        if 'model_info' and 'trimmed_uploaded_data' in st.session_state:
            model_data = st.session_state['model_info']
            uploaded_data_df = st.session_state['trimmed_uploaded_data']
            
            with st.expander("Preview Data", expanded=False):
                with st.columns([1,100,1])[1]:
                    st.dataframe(uploaded_data_df)
            
            _ = display_response(model_data)


elif selected_task == 'Predict Values':
    if 'pycaret_model' and 'uploaded_data_df' and 'pycaret_instance' in st.session_state:
        st.write("<center><h1>Predict Values</h1></center><br><br>", unsafe_allow_html=True)
        
        best_model = st.session_state['best_model']
        X_df = st.session_state['X_df']
        pycaret_instance = st.session_state['pycaret_instance']
        
        prediction_df = pd.DataFrame(
            [
                [None for _ in range(len(X_df))],
            ],  columns=X_df
        )

        edited_df = st.data_editor(prediction_df, hide_index=True, width=2000)
        
        with st.columns(len(X_df))[-1]: predict_button = st.button('Predict', use_container_width=True)
        if predict_button:
            st.write("---")
            prediction = pycaret_instance.predict_model(best_model, data=prediction_df)
            st.info(f"""
                    Predicted class/value is: **{prediction['prediction_label'].values[0]}**
                """)

    else:
        st.write("<center><h1>Predict Values</h1></center>", unsafe_allow_html=True)
        st.info("Please train a model first.")

elif selected_task == 'Download Model':
    with st.columns([1,4,1])[1]:
        st.write("<center><h1>Download Model</h1></center>", unsafe_allow_html=True)
    st.info("Please train a model first.")

elif selected_task == 'Learn ML':
    with st.columns([1,4,1])[1]:
        st.write(open('assets/html_components/learn.md', 'r').read(), unsafe_allow_html=True)

elif selected_task == 'About Us':
    with st.columns([1,4,1])[1]:
        st.write(open('assets/html_components/about.html', 'r').read(), unsafe_allow_html=True)
    st.write(open('assets/html_components/team.html', 'r').read(), unsafe_allow_html=True)