import streamlit as st

st.header('ChatGPT - Open API')


# Chat Layout
# Chat Input Kind of placeholder where user will unput his/her prompt
# chat message : display all input message by user and respinse from assistant

prompt = st.chat_input('Message')

with st.chat_message('user'):
    st.markdown(prompt)
