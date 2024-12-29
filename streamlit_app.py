import os
import streamlit as st
import openai

# Set your OpenAI API key
# Ensure OPENAI_API_KEY is set as an environment variable or replace with your actual key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app configuration
st.set_page_config(page_title="GPT-3.5 Turbo Chatbot", layout="centered", page_icon="🤖")
st.title("GPT-3.5 Turbo Chatbot")

# Input from user
user_input = st.text_input("Your prompt:", "")

if st.button("Submit"):
    if user_input:
        try:
            # Call OpenAI API with updated syntax
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_input}
                ]
            )
            # Display the response from GPT
            st.write("**Response:**")
            st.success(response["choices"][0]["message"]["content"])
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt.")

