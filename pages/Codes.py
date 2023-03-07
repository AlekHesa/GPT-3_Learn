import streamlit as st
from GPT3 import *
from streamlit_chat import message
import time


convo = [
    
]
    


st.header("Generate Your Code")
user_input = st.text_area("Generate your code",key='input')
complete = st.button("Generate your code")
if complete:
    if user_input:
        res = code_completion(user_input)
        result = res.choices[0].text
        with st.expander("Your Code"):
            st.code(result)


        
        filename = st.text_input("Your file Name & Extension")
        st.download_button(label='Download your file',data=result,file_name='try2.py')