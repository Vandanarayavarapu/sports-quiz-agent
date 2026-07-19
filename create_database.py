import json
import chromadb
from sentence_transformers import SentenceTransformer

# Load sports facts
with open("data/sports_facts.json", "r") as file:
    sports_data = json.load(file)

# Create ChromaDB client
client = chromadb.PersistentClient(path="chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="sports_facts"
)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
ids = []

# Prepare data
for index, item in enumerate(sports_data):
    documents.append(item["fact"])
    ids.append(str(index))

# Convert facts into embeddings
embeddings = model.encode(documents).tolist()

# Store in ChromaDB
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids
)

print("✅ Sports facts stored in ChromaDB successfully!")