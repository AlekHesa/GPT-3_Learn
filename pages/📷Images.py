import streamlit as st
from GPT3 import *


st.header("Image Processing")

input_prompt = st.text_input("Gambar apa yang sedang anda pikirkan?")

if input_prompt:
    try:
        image = image_process(input_prompt)
        st.image(image=image,caption=input_prompt)
    except:
        st.write("Error")

