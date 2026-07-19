import chromadb
from sentence_transformers import SentenceTransformer

# Connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

# Load collection
collection = client.get_collection(
    name="sports_facts"
)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# User query
query = "Who won the Cricket World Cup in 2011?"

# Convert query into embedding
query_embedding = model.encode([query]).tolist()

# Search database
results = collection.query(
    query_embeddings=query_embedding,
    n_results=2
)

print("Retrieved information:")
for document in results["documents"][0]:
    print("-", document)