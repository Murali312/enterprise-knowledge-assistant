import os
from dotenv import load_dotenv

import chromadb
from chromadb.utils import embedding_functions

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY is missing. Please set it in your .env file")

# -----------------------------
# Chroma client (in-memory)
# -----------------------------
client = chromadb.Client()

# -----------------------------
# Embedding function (OpenAI)
# -----------------------------
embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    api_key=OPENAI_API_KEY,
    model_name="text-embedding-3-small"
)

# -----------------------------
# Collection setup
# -----------------------------
def get_collection():
    return client.get_or_create_collection(
        name="enterprise_knowledge",
        embedding_function=embedding_function
    )

# -----------------------------
# Store embeddings (chunks)
# -----------------------------
def store_embeddings(chunks):
    collection = get_collection()

    if not chunks:
        print("⚠️ No chunks provided for embedding")
        return

    collection.add(
        documents=chunks,
        ids=[str(i) for i in range(len(chunks))]
    )

    print(f"✅ Stored {len(chunks)} chunks into vector DB")

# -----------------------------
# Query embeddings
# -----------------------------
def query_embeddings(query):
    collection = get_collection()

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    return results["documents"][0]