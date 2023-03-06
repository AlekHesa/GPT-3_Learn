import streamlit as st
from GPT3 import *
from streamlit_chat import message
import time


convo = [
    
]
    


st.header("Personal Assistant")
user_input = st.text_input("Generate your code?",key='input')
if user_input:
    convo.append({"user":user_input})
    res = code_completion(user_input)
    result = res['choices'][0]['text']
    convo.append({"assistant":res})

    with st.expander("Your Code"):
        st.code(result)
