#**MultiRAG**

A Retrieval-Augmented Generation (RAG) system for question answering over research paper content.

The system retrieves relevant text chunks using semantic vector search and uses a local LLM through Ollama to generate answers based only on the retrieved evidence.

---

## Architecture

User Question
      |
      v
Query Embedding
      |
      v
FAISS Vector Search
      |
      v
Top-K Relevant Chunks
      |
      v
Context Construction
      |
      v
Ollama / Phi-3
      |
      v
Answer


---

## Features

- Research paper question answering
- Text chunking with configurable chunk size and overlap
- Sentence Transformer embeddings
- FAISS vector similarity search
- Top-K retrieval
- Local LLM inference using Ollama
- Evidence-based answer generation
- FastAPI REST API
- Swagger/OpenAPI documentation
- Source metadata
- Request latency measurement
- Logging
- Modular project structure


---

## Tech Stack

### Programming
- Python

### Retrieval
- Sentence Transformers
- FAISS
- Dense Vector Search

### LLM
- Ollama
- Phi-3

### API
- FastAPI
- Uvicorn
- Pydantic

### Development
- Git
- GitHub


---

## Project Structure

MultiRAG/
|
├── data/
│   └── papers/
│       └── research.txt
|
├── ingestion/
│   ├── pdf_processor.py
│   ├── text_processor.py
│   └── figure_processor.py
|
├── embeddings/
│   └── embedder.py
|
├── vectorestore/
│   └── faiss_store.py
|
├── retrival/
│   └── retreiver.py
|
├── LLM/
│   └── generator.py
|
├── logs/
│   └── logger_config.py
|
├── vectorstore/
│   ├── index.faiss
│   └── metadata.json
|
├── configure.py
├── build_index.py
├── main.py
├── my_api.py
├── test_text.py
├── test_retrieval.py
├── test_llm.py
├── test_ollama.py
├── requirements.txt
├── .gitignore
└── README.md


---

## How It Works

### 1. Document Processing

The research paper is converted into text and stored as:

data/papers/research.txt

The text is divided into smaller overlapping chunks.

Current configuration:

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


### 2. Embedding Generation

Each text chunk is converted into a numerical vector using:

sentence-transformers/all-MiniLM-L6-v2

The model produces 384-dimensional embeddings.

Example:

161 chunks
    |
    v
161 x 384 embeddings


### 3. FAISS Vector Store

The generated embeddings are stored in a FAISS index.

Document chunks
      |
      v
Embeddings
      |
      v
FAISS


FAISS performs similarity search to find chunks that are semantically relevant to a user's question.


### 4. Retrieval

When a user asks a question, the question is converted into a 384-dimensional embedding.

FAISS searches the vector index and returns the most relevant chunks.

Current configuration:

TOP_K = 3


### 5. Answer Generation

The retrieved chunks are added to the LLM prompt.

The LLM is instructed to:

- Use only the provided evidence
- Avoid outside knowledge
- Avoid inventing facts
- Give concise answers
- State when the answer is not available in the retrieved evidence

The answer is generated locally using:

Ollama + Phi-3


---

## Installation

### 1. Clone the Repository

```bash
git clone <https://github.com/uday2319/Multi_RAG>
cd MultiRAG
