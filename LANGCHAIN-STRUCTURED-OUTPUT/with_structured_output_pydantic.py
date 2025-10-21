<<<<<<< HEAD
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
=======
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# schema
class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")
>>>>>>> ceb17f2 (completed langchain strucutred output)

print(result)