import streamlit as st
from chat import *
from streamlit_chat import message
import time

st.title("GPT-3 NLP")


tab1,tab2,tab3 = st.tabs(["Chatbot","Summarizer","Complete The Sentences"])
with tab1:
    st.header("GPT-3 Chatbot with Characteristics")
    def text():
        input_user = st.text_input("USER:",key="input")
        
        
        return input_user

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    characteristics = st.text_input("Characteristics",key="char")
    
    if characteristics:
        user_input = text()
        convo = list()
        convo.append('USER: %s' % user_input)
        text_block = '\n'.join(convo)
        char = characteristics + text_block+"\nJAX: "
        res = chatbot(char)

    
        if user_input:
            output = chatbot(user_input)

            st.session_state.past.append(user_input)
            st.session_state.generated.append(res)

        if st.session_state['generated']:

            for i in range(len(st.session_state['generated'])-1, -1, -1):
                message(st.session_state["generated"][i], key=str(i))
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')



