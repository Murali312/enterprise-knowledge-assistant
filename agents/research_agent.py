from crewai import Agent
from rag.vector_store import query_embeddings

def get_research_agent():
    return Agent(
        role="Research Agent",
        goal="Retrieve relevant knowledge from vector DB",
        backstory="Expert in retrieving relevant enterprise data",
        verbose=True,
        allow_delegation=False,
    )

def retrieve_context(query):
    return query_embeddings(query)