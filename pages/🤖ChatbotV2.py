import streamlit as st
from GPT3 import *
from io import StringIO
from streamlit_chat import message

convo = [
    
]
    
st.title("Welcome to Chatbot V2")

col1,col2 = st.columns([2,5])

with col1:
    st.subheader("System")
    character = st.text_area("Give your Assistant a Character")
    if character:
        convo.append(
            {"role":"system","content":character}
        )

with col2:

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    st.subheader("Chat")
    user_input = st.text_input("USER")

    if character:

        if user_input:
            convo.append(
                {"role":"user","content":user_input}
            )
            response = chatgpt_proc(convo)
            resp = response.choices[0].message.content
            convo.append(
                {"role":"assistant","content":resp}
            )

            for item in convo:
                if item["role"] == "user":
                    st.session_state.past.append(item["content"])
                if item["role"] == "assistant":
                    st.session_state.generated.append(item["content"])

            if st.session_state['generated']:

                for i in range(len(st.session_state['generated'])-1, -1, -1):
                    message(st.session_state["generated"][i], key=str(i))
                    message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            







