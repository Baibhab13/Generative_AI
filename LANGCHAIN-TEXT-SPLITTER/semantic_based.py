from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# Load your API key (from .env)
load_dotenv()

# Create the embedding model (you must have GOOGLE_API_KEY in your .env)
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-2.5-flash")

# Initialize Semantic Chunker
text_splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. 
The sun was bright, and the air smelled of earth and fresh grass. 
The Indian Premier League (IPL) is the biggest cricket league in the world. 
People all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. 
It causes harm to people and creates fear in cities and villages. 
When such attacks happen, they leave behind pain and sadness. 
To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([sample])

print(f"Number of chunks: {len(docs)}")
for i, doc in enumerate(docs, 1):
    print(f"\nChunk {i}:\n{doc.page_content}")
