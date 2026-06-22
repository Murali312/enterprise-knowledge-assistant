import os
from dotenv import load_dotenv

load_dotenv()

from rag.loader import load_documents
from rag.chunking import chunk_text
from rag.vector_store import store_embeddings

from agents.research_agent import retrieve_context
from agents.response_agent import generate_response

from evaluation.ragas_eval import evaluate_rag
from mcp.sqlite_server import init_db, log_interaction


# -----------------------------
# Setup RAG
# -----------------------------
def setup_rag():
    print("\n🚀 Application started...")
    print("📦 Initializing knowledge base...\n")

    docs = load_documents()

    all_chunks = []
    for doc in docs:
        all_chunks.extend(chunk_text(doc))

    store_embeddings(all_chunks)

    print("✅ Knowledge base ready!\n")


# -----------------------------
# Query Pipeline
# -----------------------------
def run_query(query):
    print("\n❓ Enter your question:")
    print(query)

    # STEP 1: Retrieval
    print("\n🔍 Step 1 : Retrieving relevant documents....")
    print("Generating embedding...")
    print("Searching vector database...\n")

    context = retrieve_context(query)
    context_text = " ".join(context)

    print("✅ Retrieved Context:")
    for c in context:
        print("-", c)

    # STEP 2: Agents
    print("\n🤖 Step 2 : Running CrewAI agents...")
    print("Research Agent : fetching data...")
    print("Response Agent : generating answer...")
    print("Evaluation Agent : evaluating response...\n")

    # STEP 3: Response
    response = generate_response(query, context_text)

    print("📢 Step 3 : Generating Response :\n")
    print(response)

    # STEP 4: Evaluation
    print("\n📊 Step 4 : Evaluating using RAGAS...\n")

    eval_results = evaluate_rag(query, response, context)

    print("✅ Evaluation Results :")
    for k, v in eval_results.items():
        print(f"{k} : {v}")

    # Logging
    log_interaction(query, response)


# -----------------------------
# Main loop
# -----------------------------
if __name__ == "__main__":
    init_db()
    setup_rag()

    while True:
        query = input("\n💬 Ask something (or type exit): ")

        if query.lower().strip() == "exit":
            print("\n👋 Shutting down system...")
            break

        run_query(query)