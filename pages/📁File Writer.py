import streamlit as st
from GPT3 import *


st.title("Save your paragraph to txt")

input_text = st.text_input("What do you want to write?")

if input_text:
    result = proccess_davinci(input_text)
    st.write(result)
    with open('result.txt','w') as f:
        try:
            f.write(result)
            st.write("Success")
        except:
            st.write("Error")
else:
    st.write("Please enter a prompt")

    

    
