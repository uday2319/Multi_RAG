from configure import *
from embeddings.embedder import Embedder
from ingestion.pdf_loader import load_pdf, chunk_text
from vectorestore.faiss import Faissstore
from retriver.retreiver import Retriever
import uuid
import os
from configure import *
from embeddings.embedder import Embedder

def build_rag(file_path):

    embedder = Embedder(EMBED_MODEL)
    store = Faissstore(384)

    text = load_pdf(file_path)
    chunks = chunk_text(text)

    embeddings = embedder.embed(chunks)

    metadata = [{"id": str(uuid.uuid4()), "content": c} for c in chunks]
    vectorstore_path="vectorstore/"
    os.makedirs("vectorstore",exist_ok=True)

    store.add(embeddings, metadata)
    store.save("vectorstore/") 
    import json
    with open("vectorstore/metadata.json", "w") as f:
        json.dump(metadata, f)


    retriever = Retriever(embedder, store)

    return retriever