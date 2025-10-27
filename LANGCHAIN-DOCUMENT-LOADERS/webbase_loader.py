from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

url = "https://www.python.org/"

loader = WebBaseLoader(url)

docs = loader.load()


prompt = PromptTemplate(
    template="Answer the following questions \n {question} from the follwoing text \n {text}",
    input_variables=['question','text']
)

chain = prompt | model | parser

result = chain.invoke({'question': 'What is the python?','text':docs})

print(result)