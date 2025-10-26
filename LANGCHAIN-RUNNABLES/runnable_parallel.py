from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash',temperature=0.9)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=['topic']
)

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result)
print(result['tweet'])
print(result['linkedin'])