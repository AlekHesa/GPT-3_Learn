import streamlit as st
from GPT3 import apikey
from streamlit_chat import message
import time

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("Welcome To GPT-3 Learning Showcase👋")

st.markdown(
    """
    ## What is GPT-3?
    GPT-3 is a neural network machine learning model 
    trained using internet data to generate any type of text. 
    Developed by OpenAI, it requires a small amount of input text to generate large volumes of relevant 
    and sophisticated machine-generated text.

    ## What will you showcase?
    - Chatbot
    - Code Completion
    - Images Generator
    - Natural Language Process

"""
)
with st.container():
    st.caption("Insert your API_KEY")
    api_key = st.text_input(label="your API Key",type="password")
    if api_key:
        apikey(api_key)


