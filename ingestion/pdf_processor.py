import fitz
import tiktoken
from pathlib import Path

from configure import CHUNK_SIZE, CHUNK_OVERLAP


def extract_pages(pdf_path):
    """
    Extract text from each PDF page while preserving page numbers.
    """

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    document = fitz.open(str(pdf_path))

    pages = []

    for page_number, page in enumerate(document, start=1):

        text = page.get_text("text").strip()

        if text:
            pages.append({
                "page": page_number,
                "text": text
            })

    document.close()

    return pages


def chunk_pages(pages):

    encoder = tiktoken.get_encoding("cl100k_base")

    chunks = []

    step = CHUNK_SIZE - CHUNK_OVERLAP

    for page_data in pages:

        page_number = page_data["page"]
        text = page_data["text"]

        tokens = encoder.encode(text)

        for start in range(0, len(tokens), step):

            chunk_tokens = tokens[start:start + CHUNK_SIZE]

            if not chunk_tokens:
                continue

            content = encoder.decode(chunk_tokens).strip()

            if not content:
                continue

            chunks.append({
                "content": content,
                "type": "text",
                "page": page_number
            })

    return chunks