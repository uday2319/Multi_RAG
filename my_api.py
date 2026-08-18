import time
import logging
print(logging.Logger)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from configure import EMBEDDING_MODEL, VECTORSTORE_DIR, TOP_K
from embeddings.embedder import Embedder
from vectorestore.faiss_store import FAISSStore
from retrival.retreiver import Retriever
from LLM.generator import generate_answer
from logs.logger_config import setup_logger


# -----------------------------
# Logger
# -----------------------------

logger = setup_logger()


# -----------------------------
# FastAPI
# -----------------------------

app = FastAPI(
    title="Research Paper RAG",
    description="Text-based Research Paper Question Answering System",
    version="1.0"
)


# -----------------------------
# Request model
# -----------------------------

class QueryRequest(BaseModel):
    question: str


# -----------------------------
# Create RAG system
# -----------------------------

def create_rag():

    logger.info("Initializing RAG system")

    embedder = Embedder(EMBEDDING_MODEL)

    store = FAISSStore(384)
    store.load(VECTORSTORE_DIR)

    logger.info(
        f"Vector store loaded: {store.index.ntotal} vectors"
    )

    retriever = Retriever(
        embedder,
        store
    )

    logger.info("RAG system initialized successfully")

    return retriever


retriever = create_rag()


# -----------------------------
# Root endpoint
# -----------------------------

@app.get("/")
def root():

    return {
        "message": "Research Paper RAG API is running"
    }


# -----------------------------
# Ask question
# -----------------------------

@app.post("/ask")
def ask_question(request: QueryRequest):

    start_time = time.time()

    question = request.question.strip()

    if not question:

        logger.warning("Empty question received")

        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    logger.info(f"Question received: {question}")

    try:

        # -------------------------
        # Retrieval
        # -------------------------

        results = retriever.retrieve(
            question,
            top_k=TOP_K
        )

        logger.info(
            f"Retrieved {len(results)} chunks"
        )

        # Log retrieved evidence
        for i, result in enumerate(results, start=1):

            logger.info(
                f"Retrieved chunk {i} | "
                f"source={result['source']} | "
                f"page={result['page']} | "
                f"score={result['score']:.4f}"
            )

        # -------------------------
        # Generate answer
        # -------------------------

        answer = generate_answer(
            question,
            results
        )

        logger.info("Answer generated successfully")

        # -------------------------
        # Sources
        # -------------------------

        sources = []

        for result in results:

            sources.append({
                "source": result["source"],
                "page": result["page"],
                "score": round(result["score"], 4)
            })

        # -------------------------
        # Latency
        # -------------------------

        latency = time.time() - start_time

        logger.info(
            f"Request completed | "
            f"latency={latency:.2f}s"
        )

        # -------------------------
        # Response
        # -------------------------

        return {
            "question": question,
            "answer": answer,
            "sources": sources,
            "latency_seconds": round(latency, 2)
        }

    except Exception as e:

        latency = time.time() - start_time

        logger.exception(
            f"RAG request failed | "
            f"latency={latency:.2f}s | "
            f"error={str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error while processing the question."
        )