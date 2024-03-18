import os
import webbrowser
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from st_on_hover_tabs import on_hover_tabs
from streamlit_custom_ydata_profiling import st_profile_report

try:
    from SwiftML.constants import *
    from SwiftML.utils import path_converter
    from SwiftML.model_selection.best_regressor import best_regressor

except ModuleNotFoundError:
    from constants import *
    from utils import path_converter
    from model_selection.best_regressor import best_regressor
    

c1 = 8
c2 = 0

st.set_page_config(page_title='SwiftML', page_icon=PAGE_ICON, layout='wide')

st.markdown('<style>' + open('SwiftML/assets/css/styles.css').read() if ModuleNotFoundError else open(path_converter('assets/css/styles.css')).read() + '</style>', unsafe_allow_html=True)

with st.columns([3,3,1])[2]:
    st.write(open('SwiftML/components/logo.html', 'r').read() if ModuleNotFoundError else open(path_converter('components/logo.html'), 'r').read(), unsafe_allow_html=True)

# with st.sidebar:
#     st.image('SwiftML/assets/img/LOGO.png')
#     st.write('<br><br>', unsafe_allow_html=True)
#     selected_task = on_hover_tabs(
#         tabName=['Home Page', 'Main Page', 'About Us'],
#         iconName=['home', 'task_alt', 'contact_support'],
#         styles = {
#             'navtab': {'background-color':'lightblue',
#                         'color': 'black',
#                         'font-size': '18px',
#                         'transition': '.5s',
#                         'white-space': 'nowrap',
#                         'text-transform': 'uppercase'},
#                 },
#         default_choice=1)


# uploaded_file = st.file_uploader('Upload a file', type=['csv'])
# uploaded_file = "C:/Users/arpit/My_PC/repos/SwiftML/SwiftML/assets/dataset/spg.csv"

# st.multiselect('Select Tasks', ['Model Generation', 'Save Model Locally', 'Model Deployment (beta)'])

dataset_path = st.file_uploader("Upload the dataset", type=['csv', 'xlsx'])
dataset_path = 'SwiftML/assets/dataset/spg.csv' if ModuleNotFoundError else path_converter('assets/dataset/spg.csv') if not dataset_path else dataset_path

y_col = st.empty()

data = None
if dataset_path:
    try:
        data = pd.read_csv(dataset_path, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            data = pd.read_excel(dataset_path, errors='replace')
        except Exception as e:
            st.info(f'Error reading file: {str(e)}')
    finally:
        if data is not None:
            y = y_col.selectbox('Select Target Column', data.columns[::-1])
            
st.caption("An example dataset is selected by default, press Submit to see it in action.")

submit_button_container = st.empty()
submit_button = submit_button_container.button("Submit")

if submit_button and not dataset_path:
    st.toast('Please upload the dataset', icon='⚠️')

elif submit_button and dataset_path:
    try:
        submit_button_container.empty()
        temp_container = st.empty()
        data = pd.read_csv(dataset_path)
        best_regressor(temp_container, data, y, c1, c2)

        # temp_container.empty()
        
    except Exception as e:
        st.info(f'Unable to find the best model\nError:\n{e}')


# if uploaded_file and st.button("start"):

#     df = pd.read_csv(uploaded_file)
    
#     with st.spinner('Generating Profile Report'):rp
#         pr = ProfileReport(df, title='Report')
#         pr.to_file(r'C:\Users\arpit\My_PC\repos\SwiftML\profile-report.html')
    
#     webbrowser.open(r'C:\Users\arpit\My_PC\repos\SwiftML\profile-report.html')


# with create_model_column:
#     train_button = st.button('Train Model', key='train', use_container_width=True, disabled=st.session_state['disable_button'])
#     if uploaded_file and train_button:
#         df = pd.read_csv(uploaded_file)
#         with st.spinner('Generating Profile Report'):
#             pr = ProfileReport(df, title='Report')
#             pr.to_file('./profile-report.html')
        
#         webbrowser.open(r'C:\Users\arpit\My_PC\repos\SwiftML\profile-report.html')

# with view_data_column:
#     if uploaded_file and st.button('View Data', key='view', use_container_width=True, disabled=st.session_state['disable_button']):
#         st.session_state['show_df'] = not st.session_state['show_df']

# if st.session_state['show_df']:
#     df = pd.read_csv(uploaded_file)
#     st.dataframe(df)