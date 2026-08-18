from sentence_transformers import SentenceTransformer
import numpy as np


class Embedder:

    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings.astype("float32")