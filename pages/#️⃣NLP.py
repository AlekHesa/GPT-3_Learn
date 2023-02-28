import streamlit as st
from langproc import *
from streamlit_chat import message
import time



tab1,tab2 = st.tabs(["Summarizer","Generate Text"])

    
with tab1:
    st.header("Summarization")

    input_summary = st.text_area("Put your text")

    summary = "Summarize this text :"
    sum = list()
    sum.append(input_summary)
    if input_summary: 
        test = summary + input_summary
        res = proccess(test)
        st.write(res)
    else:
        st.write("Please enter a text")   
with tab2 :
    st.header("Generate the text")
    
    input_gpt3 = st.text_input("What do you want to make?")
    
    if input_gpt3:
        res = proccess(input_gpt3)
        st.write(res)
    else:
        st.write("Please enter a text")
