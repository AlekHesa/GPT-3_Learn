import streamlit as st
from GPT3 import *
from streamlit_chat import message
import time


    
st.header("Generate Your Code")
option = st.selectbox("Choose your file Extension",('Python','Java','C'))
user_input = st.text_area("Generate your code",key='input')
complete = st.button("Generate your code")
if complete:
    if user_input:
        res = code_completion(user_input)
        result = res.choices[0].text
        with st.expander("Your Code"):
            st.code(result)
        
        if option == 'Python':
            python = 'python.py'
            st.download_button(label='Download your file',data=result,file_name=python)
        elif option == 'Java':
            java = 'Java.java'
            st.download_button(label='Download your file',data=result,file_name=java)
        elif option == 'C':
            c = 'CLang.c'
            st.download_button(label='Download your file',data=result,file_name=c)



        
        
        