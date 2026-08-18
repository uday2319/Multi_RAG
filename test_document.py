from configure import EMBEDDING_MODEL
from embeddings.embedder import Embedder


embedder = Embedder(EMBEDDING_MODEL)

texts = [
    "The Transformer uses self-attention mechanisms.",
    "The model does not use recurrence or convolution."
]

embeddings = embedder.embed(texts)

print("Shape:", embeddings.shape)
print("Data type:", embeddings.dtype)
print("First vector dimensions:", embeddings[0][:5])