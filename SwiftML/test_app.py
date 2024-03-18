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

st.set_page_config(page_title='SwiftML',
                   page_icon=PAGE_ICON,
                   layout='wide')


st.markdown('<style>' + open('SwiftML/assets/css/styles.css').read() if ModuleNotFoundError else open(path_converter('assets/css/styles.css')).read() + '</style>', unsafe_allow_html=True)

with st.columns([3,3,1])[2]:
    st.write(open('SwiftML/components/logo.html', 'r').read() if ModuleNotFoundError else open(path_converter('components/logo.html'), 'r').read(), unsafe_allow_html=True)

with st.sidebar:
    st.image('SwiftML/assets/img/LOGO.png')
    st.write('<br><br>', unsafe_allow_html=True)
    selected_task = on_hover_tabs(
        tabName=['Home Page', 'Analyse Data', 'Create Model', 'Deploy Model (beta)', 'About Us'],
        iconName=['home', 'build', 'task_alt', 'local_shipping', 'contact_support'],
        styles = {
            'navtab': {'background-color':'lightblue',
                        'color': 'black',
                        'font-size': '18px',
                        'transition': '.5s',
                        'white-space': 'nowrap',
                        'text-transform': 'uppercase'},
                },
        default_choice=1)


if 'show_df' not in st.session_state:
    st.session_state['show_df'] = False

if 'analyse_press_count' not in st.session_state:
    st.session_state['analyse_press_count'] = 0

if 'disable_button' not in st.session_state:
    st.session_state['disable_button'] = False


# uploaded_file = st.file_uploader('Upload a csv file', type=['csv'])
# uploaded_file = r'C:\Users\arpit\My_PC\repos\SwiftML\SwiftML\assets\dataset\spg.csv' if not uploaded_file else uploaded_file
uploaded_file = r'C:\Users\arpit\My_PC\repos\SwiftML\SwiftML\assets\dataset\spg.csv'

# with 'dataset' not in st.session_state:
    # st.session_state['dataset'] = uploaded_file

view_data_column, analyse_data_column, create_model_column = st.columns(3)


with analyse_data_column:
    analyse_button = st.button('Analyse Data', key='analyse', use_container_width=True, disabled=st.session_state['disable_button'])
    
    if uploaded_file and analyse_button:
        st.session_state['analyse_press_count'] += 1
        st.session_state['disable_button'] = True
        
        if st.session_state['analyse_press_count']== 1:
            
            df = pd.read_csv(uploaded_file)
            with st.spinner('Generating Profile Report'):
                pr = ProfileReport(df, title='Report')
                pr.to_file('./profile-report.html')
            
            webbrowser.open(r'C:\Users\arpit\My_PC\repos\SwiftML\profile-report.html')
            
            st.session_state['analyse_press_count'] = 0
            analyse_button.button('Analyse Data', use_container_width=True)

        elif st.session_state['analyse_press_count']> 1:
            pass

    
with create_model_column:
    train_button = st.button('Train Model', key='train', use_container_width=True, disabled=st.session_state['disable_button'])
    if uploaded_file and train_button:
        df = pd.read_csv(uploaded_file)
        with st.spinner('Generating Profile Report'):
            pr = ProfileReport(df, title='Report')
            pr.to_file('./profile-report.html')
        
        webbrowser.open(r'C:\Users\arpit\My_PC\repos\SwiftML\profile-report.html')

with view_data_column:
    if uploaded_file and st.button('View Data', key='view', use_container_width=True, disabled=st.session_state['disable_button']):
        st.session_state['show_df'] = not st.session_state['show_df']

if st.session_state['show_df']:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)