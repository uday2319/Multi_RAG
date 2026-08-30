from pathlib import Path

from configure import CHUNK_SIZE, CHUNK_OVERLAP


def read_text(file_path):

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Text file not found: {file_path}"
        )

    return file_path.read_text(
        encoding="utf-8"
    )


def chunk_text(text):

    chunks = []

    start = 0

    while start < len(text):

        end = start + CHUNK_SIZE

        chunk = text[start:end].strip()

        if chunk:

            chunks.append({
                "content": chunk,
                "type": "text"
            })

        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks