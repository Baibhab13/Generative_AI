from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large",dimensions=32)

result = embedding.embed_query("What is the capital of France?")
print(result) # Expected output: A list of floats representing the embedding vector. 
