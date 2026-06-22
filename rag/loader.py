import os

def load_documents(data_path="data"):
    docs = []
    for file in os.listdir(data_path):
        with open(os.path.join(data_path, file), "r", encoding="utf-8") as f:
            docs.append(f.read())
    return docs