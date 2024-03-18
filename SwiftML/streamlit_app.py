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

st.set_page_config(page_title="SwiftML",
                   page_icon=PAGE_ICON,
                   layout="wide")


st.markdown('<style>' + open('SwiftML/assets/css/styles.css').read() if ModuleNotFoundError else open(path_converter('assets/css/styles.css')).read() + '</style>', unsafe_allow_html=True)

misc1, misc2, misc3 = st.columns([3,3,1])

with misc3:
    st.write(open('SwiftML/components/logo.html', "r").read() if ModuleNotFoundError else open(path_converter('components/logo.html'), "r").read(), unsafe_allow_html=True)

with st.sidebar:
    st.image("SwiftML/assets/img/LOGO.png")
    st.write("<br><br>", unsafe_allow_html=True)
    selected_task = on_hover_tabs(
        tabName=['Home Page', 'View Dataset', 'Analyze Data', 'Create Model', 'Deploy Model (beta)', 'About Us'],
        iconName=['home', 'visibility', 'build', 'task_alt', 'local_shipping', 'contact_support'],
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
    st.write(open('SwiftML/components/home.html', 'r').read() if ModuleNotFoundError else open(path_converter('components/home.html'), "r").read(), unsafe_allow_html=True)

elif selected_task == 'View Data':
    with st.columns((1,5,1))[1]:
        uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])
        analyse_button_container = st.empty()
        if uploaded_file and analyse_button_container.button("View Data", key="analyze"):
            analyse_button_container.empty()
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
            
elif selected_task == 'Analyze Data':
     with st.columns((1,5,1))[1]:
        uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])
        analyse_button_container = st.empty()
        if uploaded_file and analyse_button_container.button("Analyze Data", key="analyze"):
            analyse_button_container.empty()
            df = pd.read_csv(uploaded_file)
            pr = ProfileReport(df, title="Report")
            st_profile_report(pr)
            
        # else:
        #     st.toast("Please upload a dataset", icon="⚠️")

elif selected_task == 'Create Model':
    with st.columns((1,5,1))[1]:
        dataset_path = st.file_uploader("Upload the dataset", type=['csv', 'xlsx'])
        dataset_path = path_converter('assets/dataset/spg.csv') if not dataset_path else dataset_path
        # dataset_path = 'SwiftML/assets/dataset/Red.csv' if not dataset_path else dataset_path
        
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
    with st.columns([1,5,1])[1]:
        # st.write(open(path_converter('components/about.html'), "r").read(), unsafe_allow_html=True)
        st.write(open('SwiftML/components/about.html', "r").read(), unsafe_allow_html=True)
        
elif selected_task == 'Deploy App (beta)':
    st.write(open(path_converter('components/deploy.html'), "r").read(), unsafe_allow_html=True)
    # st.write(open('SwiftML/components/deploy.html', "r").read(), unsafe_allow_html=True)

else:
    st.write("<center><h1>{}</h1></center>".format(selected_task.title()), unsafe_allow_html=True)