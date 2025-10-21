from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

#schema
# class Review(TypedDict):
    
#     summary: str
#     sentiment: str
# 

# Annotated description for better clarity in the output
class Review(TypedDict):
    key_themes: Annotated[str, "Key themes mentioned in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Overall sentiment of the review, e.g., positive, negative, neutral"]
    pros: Annotated[Optional[list[str]], "Positive aspects mentioned in the review"]
    cons: Annotated[Optional[list[str]], "Negative aspects mentioned in the review"]
    name: Annotated[Optional[str], "Name of the reviewer if mentioned"]
 
model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The hardware is great, but software feels bloated. There are too many pre-installed apps that I can't remove. ALso, the UI looks outdated compared to other brands. Hoping for a software update to fix this.")

print(result)