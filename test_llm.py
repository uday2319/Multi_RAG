from LLM.generator import generate_answer


query = "What is retrieval augmented generation?"

context_chunks = [
    {
        "source": "research.txt",
        "page": "1",
        "content": """
        Retrieval-Augmented Generation (RAG) combines
        retrieval of external knowledge with generation
        by a language model.
        """
    }
]


answer = generate_answer(
    query,
    context_chunks
)

print("\nANSWER:")
print(answer)