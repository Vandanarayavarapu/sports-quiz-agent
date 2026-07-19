import json
import chromadb
from sentence_transformers import SentenceTransformer

# Connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create collection if it does not exist
collection = client.get_or_create_collection(
    name="sports_facts"
)

# Add data if collection is empty
if collection.count() == 0:

    with open("data/sports_facts.json", "r") as file:
        sports_data = json.load(file)

    documents = []
    ids = []

    for index, item in enumerate(sports_data):
        documents.append(item["fact"])
        ids.append(str(index))

    embeddings = model.encode(documents).tolist()

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )

print("Sports database ready!")