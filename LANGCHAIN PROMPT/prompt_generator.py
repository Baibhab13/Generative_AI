from langchain_core.prompts import PromptTemplate   

# template
template = PromptTemplate(

    template = """
    Summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details: 
    - Include relevant equations and mathematical concepts.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
    2. Analogies:
    - Use Relatable analogies to simplify compex ideas.
    if certain information is not available, resonse with: "Insufficient information to summarize the paper." instead of guessing.
    Ensure the summary is clear, accurate and aligns with the specified style and length.
""",
    input_variables = ["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save('template.json')  # Save the template to a JSON file