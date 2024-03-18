import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from st_on_hover_tabs import on_hover_tabs
from streamlit_pandas_profiling import st_profile_report

from SwiftML.constants import *
from SwiftML.utils import path_converter
from SwiftML.model_selection.best_regressor import best_regressor


c1 = 8
c2 = 0

st.set_page_config(page_title="UnityML", 
                   page_icon=PAGE_ICON,
                   layout="wide")

st.markdown('<style>' + open(path_converter('assets/css/styles.css')).read() + '</style>', unsafe_allow_html=True)
# st.markdown('<style>' + open('unityml/assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)

misc1, misc2, misc3 = st.columns([3,3,1])

with misc3:
    st.write(open(path_converter('components/logo.html'), "r").read(), unsafe_allow_html=True)
    # st.write(open('unityml/components/logo.html', "r").read(), unsafe_allow_html=True)

with st.sidebar:
    selected_task = on_hover_tabs(
        tabName=['Home Page', 'Analyze Data', 'Create Model', 'Deploy App (beta)', 'About Us'],
        iconName=['home', 'psychology', 'build', 'task_alt', 'contact_support'],
        styles = {
            'navtab': {'background-color':'lightblue',
                        'color': 'black',
                        'font-size': '18px',
                        'transition': '.5s',
                        'white-space': 'nowrap',
                        'text-transform': 'uppercase'},
                },
        default_choice=1)


if selected_task == 'Home Page':
    st.write(open(path_converter('components/home.html'), "r").read(), unsafe_allow_html=True)
    # st.write(open('unityml/components/home.html', 'r').read(), unsafe_allow_html=True)

elif selected_task == 'Analyze Data':
     _, main, _ = st.columns((1,5,1))
     
     with main:
        uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])
        analyse_button_container = st.empty()
        analyse_button = analyse_button_container.button("Analyze Data")
        if analyse_button and uploaded_file:
            df = pd.read_csv(uploaded_file)
            pr = ProfileReport(df, title="Report")
            st_profile_report(pr)
        elif analyse_button and not uploaded_file:
            st.toast("Please upload a file", icon="⚠️")

elif selected_task == 'Create Model':
    _, main, _ = st.columns((1,5,1))    

    with main:
        dataset_path = st.file_uploader("Upload the dataset", type=['csv', 'xlsx'])
        dataset_path = path_converter('assets/dataset/spg.csv') if not dataset_path else dataset_path
        # dataset_path = 'unityml/assets/dataset/Red.csv' if not dataset_path else dataset_path
        
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
            
elif selected_task == 'About Us':
    st.write(open(path_converter('components/about.html'), "r").read(), unsafe_allow_html=True)
    # st.write(open('unityml/components/about.html', "r").read(), unsafe_allow_html=True)

elif selected_task == 'Deploy App (beta)':
    st.write(open(path_converter('components/deploy.html'), "r").read(), unsafe_allow_html=True)
    # st.write(open('unityml/components/deploy.html', "r").read(), unsafe_allow_html=True)

else:
    st.write("<center><h1>{}</h1></center>".format(selected_task.title()), unsafe_allow_html=True)