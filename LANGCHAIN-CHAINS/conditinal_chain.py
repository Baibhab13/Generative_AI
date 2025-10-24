from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

parser = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description="give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following text into positive, negative feedback \n {feedback} \n {format_instructions}",
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write a appropriate response to the following positive feedback: \n {feedback} ",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write a appropriate response to the following negative feedback: \n {feedback} ",
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({'feedback': 'The product quality is very bad and delivery was late'}).sentiment

# print(result)

# branch_chain = RunnableBranch(
#     (condition1: chain1),
#     (condition2: chain2)
# )

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a terrible phone'}))

chain.get_graph().print_ascii()