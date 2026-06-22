from crewai import Agent

def get_evaluation_agent():
    return Agent(
        role="Evaluation Agent",
        goal="Evaluate answer quality using RAGAS",
        backstory="Expert in evaluating LLM outputs",
        verbose=True,
    )