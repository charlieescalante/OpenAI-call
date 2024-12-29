import streamlit as st
import openai

# Load the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

# Set up the Streamlit app
st.title("GPT-3.5 Turbo Chatbot")
st.write("Enter a prompt and receive a response from GPT-3.5 Turbo.")

# Input text box for user prompt
user_input = st.text_input("Your prompt:")

# Function to get response from OpenAI
def get_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Display the response when the user submits a prompt
if st.button("Submit"):
    if user_input:
        with st.spinner("Generating response..."):
            response = get_gpt_response(user_input)
        st.write("**Response:**")
        st.write(response)
    else:
        st.warning("Please enter a prompt.")
