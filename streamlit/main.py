import pandas as pd
import streamlit as st
from pycaret.regression import *

from reg_utils import best_regressor

st.set_page_config(layout="wide")

left, main, right = st.columns((1,2,1))

with left and right:
    st.empty()
    
with main:
    # st.write('<center><h1>Unity ML</h1></center><br><br>', unsafe_allow_html=True)
    dataset_path = st.file_uploader("Upload the dataset", type=['csv'])
    dataset_path = r"test\spg.csv" if not dataset_path else dataset_path
    
    y_col = st.empty()
    y = y_col.selectbox('Select Target Column', ['Please upload the dataset first'])

    if dataset_path:
        data = pd.read_csv(dataset_path)
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
            best_regressor(temp_container, st, data, y)
            # temp_container.empty()
            st.balloons()
            
        except Exception as e:
            st.info(f'Unable to find the best model\nError:\n{e}')