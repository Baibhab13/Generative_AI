from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = "Tell me 5 interesting facts about {topics}",
    input_variables=['topics']
)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature = 0)

parser = StrOutputParser()

#  The process of making chain using the pipe oerator '|' -> Langchain expression Language
chain = prompt | model| parser

result = chain.invoke({'topics': 'blackhole'})

print(result)

chain.get_graph().print_ascii()