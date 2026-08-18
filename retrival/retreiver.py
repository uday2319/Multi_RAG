class Retriever:

    def __init__(self, embedder, vectorstore):
        self.embedder = embedder
        self.vectorstore = vectorstore

    def retrieve(self, query, top_k=5):

        query_embedding = self.embedder.embed([query])

        results = self.vectorstore.search(
            query_embedding,
            top_k=top_k
        )

        return results