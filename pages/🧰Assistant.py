import streamlit as st
from GPT3 import *
from io import StringIO
from streamlit_chat import message

convo = [
    {"role":"system","content":"You are a helpful assistant"}
]
    


st.header("Personal Assistant")
user_input = st.text_input("What would you like to know?",key='input')
if user_input:
    convo.append({"role":"user","content":user_input})
    gpt3 = chatgpt_proc(convo)
    convo.append({"role":"assistant","content": gpt3['choices'][0]['message']['content']})
    st.write(gpt3['choices'][0]['message']['content'])          
     

