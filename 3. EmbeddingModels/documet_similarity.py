from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Paris is the capital of France.",
    "Berlin is the capital of Germany.",
    "Madrid is the capital of Spain.",
    "Cristiano Ronaldo is a football player",
    "Neymar is a football player",
    "Ms Dhoni is a former Indian cricket team captain",
    "Virat Kohli is the current captain of the Indian cricket team"
]

query = "Who is the captain of the Indian cricket team?"

doc_embeddings =  embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)  

score = cosine_similarity([query_embedding], doc_embeddings)[0]

index, scores = sorted(list(enumerate(score)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("similarity score: ", scores)