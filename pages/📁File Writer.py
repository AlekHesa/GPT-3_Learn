import streamlit as st
from GPT3 import *
from io import StringIO



st.header("Upload your file")

readpath = st.file_uploader("Upload your text")
if readpath is not None:
    stringio = StringIO(readpath.getvalue().decode('utf-8'))
    readfile = stringio.read()
    result = proccess_davinci(readfile)

    btn_result = st.button("Proccess")
    if btn_result:
        st.write(readfile)



    

    
