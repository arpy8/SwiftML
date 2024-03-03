import pandas as pd
import streamlit as st
from st_on_hover_tabs import on_hover_tabs

from unityml.utils import *
from unityml.constants import *
from unityml.best_reg import best_regressor

st.set_page_config(page_title="UnityML", 
                   page_icon=PAGE_ICON,
                   layout="wide")


st.markdown('<style>' + open(path_converter('assets/css/styles.css')).read() + '</style>', unsafe_allow_html=True)
# st.markdown('<style>' + open('unityml/assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)

misc1, misc2, misc3 = st.columns([3,3,1])

with misc3:
    st.write(open(path_converter('components/logo.html'), "r").read(), unsafe_allow_html=True)

with st.sidebar:
    selected_task = on_hover_tabs(
        tabName=['Home', 'Create Model', 'Deploy App', 'About Us'],
        iconName=['home', 'psychology', 'task_alt', 'contact_support'],
        styles = {
            'navtab': {'background-color':'lightblue',
                        'color': 'black',
                        'font-size': '18px',
                        'transition': '.5s',
                        'white-space': 'nowrap',
                        'text-transform': 'uppercase'},
                },
        default_choice=0)


if selected_task == 'Home':
    st.write(open(path_converter('components/home.html'), "r").read(), unsafe_allow_html=True)
    # st.write(open('unityml/components/home.html', 'r').read(), unsafe_allow_html=True)

elif selected_task == 'Create Model':
    left, main, right = st.columns((1,2,1))

    with left and right:
        st.empty()
        
    with main:
        dataset_path = st.file_uploader("Upload the dataset", type=['csv', 'xlsx'])
        dataset_path = path_converter('assets/dataset/spg.csv') if not dataset_path else dataset_path
        
        y_col = st.empty()
        y = y_col.selectbox('Select Target Column', ['Please upload the dataset first'])
        
        data = None

        if dataset_path:
            try:
                data = pd.read_csv(dataset_path, encoding='utf-8')
            except UnicodeDecodeError:
                data = pd.read_excel(dataset_path, errors='replace')
            finally:
                y = y_col.selectbox('Select Target Column', data.columns[::-1])
          
        submit_base = st.empty()
        submit = submit_base.button("Submit")

        if submit and not dataset_path:
            st.toast('Please upload the dataset', icon='⚠️')

        elif submit and dataset_path:
            try:
                submit_base.empty()
                temp_container = st.empty()
                data = pd.read_csv(dataset_path)
                best_regressor(temp_container, data, y)
                # temp_container.empty()
                st.balloons()
                
            except Exception as e:
                st.info(f'Unable to find the best model\nError:\n{e}')
            
    # st.write(open(path_converter('components/create_model.html'), "r").read(), unsafe_allow_html=True)
    # st.write(open('unityml/components/create_model.html', "r").read(), unsafe_allow_html=True)

elif selected_task == 'About Us':
    # team_members()
    st.write(open(path_converter('components/about.html'), "r").read(), unsafe_allow_html=True)
    # st.write(open('unityml/components/about.html', "r").read(), unsafe_allow_html=True)
    
else:
    st.write("<center><h1>{}</h1></center>".format(selected_task.title()), unsafe_allow_html=True)