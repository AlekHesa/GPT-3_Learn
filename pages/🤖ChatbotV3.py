import streamlit as st
from GPT3 import *
from io import StringIO
from streamlit_chat import message

convo = [
    
]

list_of_filter = ['what','where','who','why','when','how','siapa','dimana','bagaimana','kapan','apa','hello']
    
st.title("Welcome to AG-BOT")

prompt = """
    You are an AI named AG-BOT that can help user to solve problems and also user can ask you a question about a certain words to know its meaning
    and description. The problem that they can ask is related to Astragraphia needs such as digital printing, information technology, and any
    technology related topic. if user ask anything that is not related to the topic mentioned before, do not answer the question and say 'please do not ask anything other than the topic i mention'
    """
if prompt:
    char = {"role":"system","content":prompt}
    convo.append(char)


if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

st.subheader("Chat")
user_input = st.text_area("USER")



if user_input:
    for filter in list_of_filter:
        if filter in user_input:
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
        








