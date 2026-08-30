from ingestion.pdf_processor import read_text, chunk_text

text_path = "data/papers/research.txt"

text = read_text(text_path)

print("Characters extracted:", len(text))

chunks = chunk_text(text)

print("Chunks created:", len(chunks))

for chunk in chunks[:3]:

    print("\n----------------")

    print("Chunk:")
    print(chunk["content"][:500])