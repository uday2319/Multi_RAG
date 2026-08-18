import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
LLM_MODEL = "phi3"


def generate_answer(query, context_chunks):

    context_parts = []

    for chunk in context_chunks:

        context_parts.append(
            f"""
Source: {chunk["source"]}
Page: {chunk["page"]}

{chunk["content"]}
"""
        )

    context = "\n".join(context_parts)

    prompt = f"""
You are a research paper question-answering assistant.

Answer the question ONLY using the provided evidence.

Rules:
1. Do not use outside knowledge.
2. Do not invent facts or numbers.
3. If the evidence does not contain the answer, say exactly:
Answer not found in the paper.
4. Give a concise and direct answer.
5. When possible, mention the page number supporting the answer.

EVIDENCE:
{context}

QUESTION:
{query}

ANSWER:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": LLM_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"].strip()