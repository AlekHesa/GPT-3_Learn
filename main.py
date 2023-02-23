import streamlit as st
from chat import *
from streamlit_chat import message

st.title("JAX the machine for World Peace!")

def text():
    input_user = st.text_input("USER:",key=input)
    return input_user

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input = text()

if user_input:
    output = gpt3_completion(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


if st.button("CLEAR CHAT"):
    st.session_state.clear()
