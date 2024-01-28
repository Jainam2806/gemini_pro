from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question).text
    return response

# Streamlit window setup
st.set_page_config(page_title="Google Gemini-Pro")
st.title("Google Gemini-Pro")
# user_input = st.text_input("Enter your question:", key="user_input")
user_input = st.text_area("Input Prompt: ", key="user_input", height=150)

submit_button = st.button("Submit", key="submit_button")

if user_input and not submit_button:
    submit_button = True

if submit_button:
    response = get_gemini_response(question=user_input)
    st.text_area("Response:", response, height=300)
