from configure import (
    EMBEDDING_MODEL,
    PAPERS_DIR,
    VECTORSTORE_DIR
)

from ingestion.pdf_processor import (
    extract_pages,
    chunk_pages
)

from embeddings.embedder import Embedder
from vectorestore.faiss_store import FAISSStore


pdf_path = PAPERS_DIR / "research_paper.pdf"

# 1. Extract
pages = extract_pages(pdf_path)

# 2. Chunk
chunks = chunk_pages(pages)

# Add source metadata
for chunk in chunks:
    chunk["source"] = pdf_path.name

print("Chunks:", len(chunks))

# 3. Embed
embedder = Embedder(EMBEDDING_MODEL)

texts = [
    chunk["content"]
    for chunk in chunks
]

embeddings = embedder.embed(texts)

print("Embeddings:", embeddings.shape)

# 4. FAISS
dimension = embeddings.shape[1]

store = FAISSStore(dimension)

store.add(
    embeddings,
    chunks
)

# 5. Save
store.save(VECTORSTORE_DIR)

print("Vector store created successfully.")