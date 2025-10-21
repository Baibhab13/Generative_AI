from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large",dimensions=32)

documents = [
    "Paris is the capital of France.",
    "Berlin is the capital of Germany.",
    "Madrid is the capital of Spain."
]
result = embedding.embed_documents(documents)
print(str(result)) # Expected output: A list of floats representing the embedding vector. 
