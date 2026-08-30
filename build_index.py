from configure import (
    EMBEDDING_MODEL,
    PAPERS_DIR,
    VECTORSTORE_DIR
)

from ingestion.pdf_processor import (
    read_text,
    chunk_text
)

from embeddings.embedder import Embedder
from vectorestore.faiss_store import FAISSStore


# Text file
text_path = PAPERS_DIR / "research.txt"


# 1. Read text
text = read_text(text_path)

print("Characters:", len(text))


# 2. Chunk text
chunks = chunk_text(text)

# Add source metadata
for chunk in chunks:
    chunk["source"] = text_path.name


print("Chunks:", len(chunks))


# 3. Create embeddings
embedder = Embedder(EMBEDDING_MODEL)

texts = [
    chunk["content"]
    for chunk in chunks
]

embeddings = embedder.embed(texts)

print("Embeddings:", embeddings.shape)


# 4. Create FAISS index
dimension = embeddings.shape[1]

store = FAISSStore(dimension)

store.add(
    embeddings,
    chunks
)


# 5. Save vector store
store.save(VECTORSTORE_DIR)

print("Vector store created successfully.")