from ingestion.pdf_processor import extract_pages, chunk_pages

pdf_path = "data/papers/reseaarch_paper.pdf"

pages = extract_pages(pdf_path)

print("Pages extracted:", len(pages))

chunks = chunk_pages(pages)

print("Chunks created:", len(chunks))

for chunk in chunks[:3]:
    print("\n----------------")
    print("Page:", chunk["page"])
    print("Type:", chunk["type"])
    print(chunk["content"][:500])