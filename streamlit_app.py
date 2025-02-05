import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets['OPENAI_API_Key'])
st.header('ChatGPT - Open API')


# initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

#displays all chat history information
# messages
# {'role' : "user" or "assistant" or "system", "content" : prompt or response}
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Chat Layout
# Chat Input Kind of placeholder where user will unput his/her prompt
# chat message : display all input message by user and respinse from assistant


if prompt := st.chat_input('Message'):
    msg = {
        'role' : 'user' ,
        'content' : prompt
    }
    st.session_state.messages.append(msg)

with st.chat_message('user'):
    st.markdown(prompt)

with st.chat_message('assistant'):
    
    # Create Chat Completion API
    chatresponse = client.chat.completions.create(
        model='chatgpt-4o-latest',
        messages= st.session_state.messages,
        temperature=1,
        n=1,
        stream=True
    )
    response_content = st.write_stream(chatresponse)

st.session_state.messages.append(
    {"role":"assistant",
     "content": response_content}
)

#how this all works is explained here: https://www.youtube.com/watch?v=k1RzpXQ6MXc





