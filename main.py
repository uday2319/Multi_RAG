from configure import EMBEDDING_MODEL, VECTORSTORE_DIR, TOP_K

from embeddings.embedder import Embedder
from vectorestore.faiss_store import FAISSStore
from retrival.retreiver import Retriever
from LLM.generator import generate_answer


def create_rag():

    embedder = Embedder(EMBEDDING_MODEL)

    store = FAISSStore(384)
    store.load(VECTORSTORE_DIR)

    retriever = Retriever(
        embedder,
        store
    )

    return retriever


def main():

    retriever = create_rag()

    print("Research Paper RAG")
    print("Type 'exit' to quit.")

    while True:

        query = input("\nAsk: ")

        if query.lower() == "exit":
            break

        results = retriever.retrieve(
            query,
            top_k=TOP_K
        )

        answer = generate_answer(
            query,
            results
        )

        print("\nAnswer:")
        print(answer)

        print("\nSources:")

        for result in results:
            print(
                f"- {result['source']} "
                f"(Page {result['page']}, "
                f"score={result['score']:.3f})"
            )


if __name__ == "__main__":
    main()