import time
import pickle
import base64
import pandas as pd
import streamlit as st
from st_on_hover_tabs import on_hover_tabs

from constants import BACKGROUND, PAGE_ICON, MODEL_DETAILS_TEMPLATE 
from train_model import process_dataset, display_response


st.set_page_config(page_title='SwiftML', page_icon=PAGE_ICON, layout='wide')

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
        default_choice=0)

if selected_task == 'Home Page':
    st.write(open('assets/html_components/home.html', 'r').read(), unsafe_allow_html=True)

elif selected_task == 'Process Dataset':
    try:
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
                                )
            
            with dataset_option_columns[1]:
                st.write("##### Select Target Type")
                problem_type = st.selectbox(
                                    label='Select Target Type', 
                                    options=["Classification", "Regression"], 
                                    label_visibility="hidden", 
                                    disabled=False
                                )
            
            with dataset_option_columns[2]: 
                st.write("##### Select Extra Columns")
                metadata_columns = st.multiselect(
                                        label='Select Extra Columns', 
                                        options=[i for i in uploaded_data_df.columns if i!=target], 
                                        label_visibility="hidden",
                                        placeholder="Select extra columns to drop"
                                    )
                trimmed_uploaded_data = uploaded_data_df[[column for column in uploaded_data_df.columns if column not in metadata_columns]]
                

            with dataset_option_columns[3]:
                st.write("<br><br>", unsafe_allow_html=True)
                submit_uploaded_file_container = st.empty()
                
            uploaded_data_container.dataframe(trimmed_uploaded_data, hide_index=True, width=2000)
            if submit_uploaded_file_container.button(label='Submit', use_container_width=True):
                header_container.empty()
                submit_uploaded_file_container.empty()
                st.write("---")
                
                start_time = time.time()
                
                with st.spinner("Processing data..."):
                    api_response  = process_dataset(trimmed_uploaded_data, target, problem_type.lower())
                
                if api_response:
                    display_response()
                
                submit_uploaded_file_container.button(label='Submit', use_container_width=True, key='submit_button2')
                    
                end_time = time.time()
                st.toast(f"Processed finished in : {end_time-start_time:.2f} seconds.")

        else:
            if "final_model" in st.session_state:
                with st.expander("Preview Data", expanded=False):
                    with st.columns([1,100,1])[1]:
                        st.dataframe(st.session_state['data'], hide_index=True, width=2000)
                
                display_response()
                
            
    except UnicodeDecodeError:
        st.error('Error reading file: UnicodeDecodeError')


elif selected_task == 'Predict Values':
    if "final_model" in st.session_state:
        st.write("<center><h1>Predict Values</h1></center><br><br>", unsafe_allow_html=True)
        st.caption("We've automatically populated the values from the test dataset. Feel free to edit them.")
        
        final_model = st.session_state['final_model']
        X_train_columns = st.session_state['X_train_columns']
        pycaret_base = st.session_state['pycaret_base']
        
        prediction_df = pd.DataFrame(
            [
                st.session_state['X_test'][0],
            ],  columns=X_train_columns
        )
        
        edited_df = st.data_editor(prediction_df, hide_index=True, width=2000)
        
        with st.columns(len(X_train_columns))[-1]: predict_button = st.button('Predict', use_container_width=True)
        if predict_button:
            st.write("---")
            prediction = pycaret_base.predict_model(final_model, data=prediction_df)
            st.info(f"""
                    Predicted class/value is: **{prediction['prediction_label'].values[0]}**
                """)
    else:
        st.write("<center><h1>Predict Values</h1></center><br><br>", unsafe_allow_html=True)
        st.info("Please train a model first.")

elif selected_task == 'Download Model':
    with st.columns([1,4,1])[1]:
        st.write("<center><h1>Download Model</h1></center><br><br>", unsafe_allow_html=True)
    if "final_model" in st.session_state:
        st.write(MODEL_DETAILS_TEMPLATE.format(
                model_name=st.session_state['model_name'], 
                final_model=str(st.session_state['final_model']), 
                model_definition=st.session_state['model_definition'], 
                model_info_link=st.session_state['model_info_link']
        ), unsafe_allow_html=True)
        
        with open('final_model.pkl', 'wb') as f:
            pickle.dump(st.session_state['final_model'], f)

        st.write("Click the button below to download the trained model.")
        st.download_button(label='Download Model', data=open('final_model.pkl', 'rb').read(), file_name='final_model.pkl', mime='application/octet-stream', use_container_width=True)
            
    else:
        st.info("Please train a model first.")

elif selected_task == 'Learn ML':
    with st.columns([1,4,1])[1]:
        st.write(open('assets/html_components/learn.md', 'r').read(), unsafe_allow_html=True)

elif selected_task == 'About Us':
    with st.columns([1,4,1])[1]:
        st.write(open('assets/html_components/about.html', 'r').read(), unsafe_allow_html=True)
    st.write(open('assets/html_components/team.html', 'r').read(), unsafe_allow_html=True)