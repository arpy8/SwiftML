import base64
import pandas as pd
import streamlit as st
from st_on_hover_tabs import on_hover_tabs

try:
    from SwiftML.__constants import *
    from SwiftML.__utils import path_convertor
    from SwiftML.__model_creation import process_dataset
    from __constants import BACKGROUND

except ModuleNotFoundError:
    from __utils import path_convertor
    from __model_creation import process_dataset
    from __constants import BACKGROUND


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
        header_css=open('SwiftML/assets/css/styles.css').read() if ModuleNotFoundError else open(path_convertor('assets/css/styles.css')).read(),
        bin_str=bin_str
    )
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_page_background(BACKGROUND)

with st.columns([3,3,1])[2]:
    st.write(open('SwiftML/html_components/logo.html', 'r').read() if ModuleNotFoundError else open(path_convertor('html_components/logo.html'), 'r').read(), unsafe_allow_html=True)

with st.sidebar:
    # with st.columns([1,10,1])[1]:
    # st.image('SwiftML/assets/img/logo2.png')
    
    st.write('<br><br>', unsafe_allow_html=True)
    selected_task = on_hover_tabs(
        tabName=['Homepage', 'Process Data', 'How to Use', 'Learn', 'About Us'],
        iconName=['home', 'engineering', 'info','school', 'contact_support'],
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
        
        key="2",
        default_choice=0)


if selected_task == 'Homepage':
    st.write(open('SwiftML/html_components/home.html', 'r').read() if ModuleNotFoundError else open(path_convertor('html_components/home.html'), "r").read(), unsafe_allow_html=True)

elif selected_task == 'Process Data':
    st.write("""
            <div style='text-align:center;'>
                <h1 style='text-align:center; font-size: 300%;'>Process Data</h1>
                <p style=' color: #9c9d9f'>Upload your dataset and watch us do the magic.</p>
                <hr>
            </div>
             """, unsafe_allow_html=True)
    
    # uploaded_file = r"C:\Users\arpit\My_PC\repos\SwiftML\SwiftML\assets\dataset\Iris.csv"
    uploaded_file = st.file_uploader('Please upload a dataset', type=['csv'])
    
    columns = st.columns([9,9,4])
    
    with columns[0]:
        if uploaded_file:
            uploaded_data = pd.read_csv(uploaded_file)
            st.write("##### Select Target Column")
            target = st.selectbox('Select Target Column', uploaded_data.columns[::-1], label_visibility="hidden", disabled=st.session_state['disable_button'])
    
    with columns[1]:
        if uploaded_file:
            st.write("##### Select Target Type")
            query = st.selectbox('Select Target Type', ["Regression", "Classification"], label_visibility="hidden", disabled=st.session_state['disable_button'])
    
    with columns[2]:
        st.write("<br><br>", unsafe_allow_html=True)
        submit_uploaded_file_container = st.empty()
    
    if uploaded_file is not None and submit_uploaded_file_container.button('Submit', use_container_width=True):
        submit_uploaded_file_container.empty()
        st.write("---")
        
        query = 'cls' if query == 'Classification' else 'reg' if query in ['Regression', 'Classification'] else None
        
        try:
            process_dataset(uploaded_data, target, query)
                
        except UnicodeDecodeError:
            st.error('Error reading file: UnicodeDecodeError')
        except Exception as e:
            st.error('Error reading file: ' + str(e))
        
elif selected_task == 'How to Use':
    with st.columns([1,4,1])[1]:
            st.write(open('SwiftML/html_components/doc.md', 'r').read() if ModuleNotFoundError else open(path_convertor('html_components/about.html'), "r").read(), unsafe_allow_html=True)

elif selected_task == 'Learn':
    with st.columns([1,4,1])[1]:
        st.write(open('SwiftML/html_components/learn.md', 'r').read() if ModuleNotFoundError else open(path_convertor('html_components/about.html'), "r").read(), unsafe_allow_html=True)

elif selected_task == 'About Us':
    with st.columns([1,4,1])[1]:
        st.write(open('SwiftML/html_components/about.html', 'r').read() if ModuleNotFoundError else open(path_convertor('html_components/about.html'), "r").read(), unsafe_allow_html=True)
    st.write(open('SwiftML/html_components/team.html', 'r').read() if ModuleNotFoundError else open(path_convertor('html_components/about.html'), "r").read(), unsafe_allow_html=True)