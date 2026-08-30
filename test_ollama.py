import requests
import time

url = "http://localhost:11434/api/generate"

for i in range(5):

    start = time.time()

    response = requests.post(
        url,
        json={
            "model": "phi3",
            "prompt": "What is RAG? Answer in one sentence.",
            "stream": False,
            "options": {
                "num_predict": 50,
                "temperature": 0.1
            }
        },
        timeout=120
    )

    elapsed = time.time() - start

    print(f"Request {i + 1}: {elapsed:.2f}s")