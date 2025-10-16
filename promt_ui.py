from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

st.header('Research Paper Summarizer')

user_input =  st.text_input("Enter you prompt")

if st.button('Submit'):
    result  =  model.invoke(user_input)
    st.write(result.content)
