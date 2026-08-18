📚 Multi_RAG

A scalable Multi-Document Retrieval-Augmented Generation (RAG) system that enables querying across multiple knowledge sources using FAISS vector search and local LLMs via Ollama (Qwen and others).

🚀 Overview:
Performs context-aware question answering over multiple documents
Uses FAISS for fast vector similarity search
Integrates Ollama-hosted LLMs (Qwen, LLaMA, etc.) for local inference
Designed for modularity, performance, and offline capability

🧠 Key Features:
🔎 Multi-document retrieval
🧩 Context aggregation from multiple sources
⚡ High-speed similarity search with FAISS
🏠 Fully local LLM support via Ollama (no API dependency)
🔌 Easily extendable to new models and vector stores

🏗️ Architecture:
Data Ingestion
Load documents (PDF, TXT, etc.)
Split into smaller chunks
Embedding Generation
Convert chunks into vector embeddings
Vector Store (FAISS)
Store embeddings for fast retrieval
Retriever
Fetch top-k relevant chunks for a query
LLM (Ollama)
Generate final response using retrieved context

⚙️ Tech Stack:
Python
FAISS (vector database)
Ollama (local LLM serving)
Qwen

File Architecture :
Multi_RAG/
│── data/              # Input documents
│── embeddings/        # Stored vectors
│── src/
│   ├── ingestion.py
│   ├── retriever.py
│   ├── generator.py
│── app.py             # Main entry point
│── requirements.txt
│── README.md

Use Cases:
💬 Chat with multiple documents
📊 Enterprise knowledge assistant
📖 Research & document analysis
🤝 Customer support automation
