from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def get_response_agent():
    return Agent(
        role="Response Generator",
        goal="Generate accurate answers",
        backstory="Expert in answering enterprise queries",
        llm=llm,
        verbose=True,
    )

def generate_response(query, context):
    prompt = f"""
    Answer the question using context only.

    Context:
    {context}

    Question:
    {query}
    """
    return llm.invoke(prompt).content