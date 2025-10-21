# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model  = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

# result = model.invoke("What is the capital of India")
# print(result.content)


import os
import google.generativeai as genai
genai.configure(api_key='YOUR_API_KEY')
for m in genai.list_models():
    print(m.name)
