from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
PAPERS_DIR = DATA_DIR / "papers"
FIGURES_DIR = DATA_DIR / "figures"
VECTORSTORE_DIR = BASE_DIR / "vectorstore"

# Models
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Retrieval
TOP_K = 5

# Chunking
CHUNK_SIZE = 400
CHUNK_OVERLAP = 80

# Create directories
PAPERS_DIR.mkdir(parents=True, exist_ok=True)
FIGURES_DIR.mkdir(parents=True, exist_ok=True)
VECTORSTORE_DIR.mkdir(parents=True, exist_ok=True)