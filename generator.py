import requests
def generate_answer(query,context_chunks):
    context="\n".join(item["content"] for item in context_chunks)
    #print("RETRIEVED CONTEXT:\n", context)

    prompt = f"""
Answer ONLY using the provided context.
If the answer is not explicitly present in the context,
respond exactly with:
Answer not found in document.
Do not add anything else.
Context:
{context}

Question:
{query}

Give the exact number from the document.
Answer:
"""
    response=requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model":"phi3",
            "prompt":prompt,
            "stream":False
        }
    )
    return response.json()["response"]