import os
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""

    text = ""

    try:
        reader = PdfReader(pdf_path)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception as e:
        return f"Error reading PDF: {e}"


def split_text(text, chunk_size=1000):
    """Split text into smaller chunks."""

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]

        if chunk.strip():
            chunks.append(chunk.strip())

    return chunks


def search_chunks(chunks, query, top_k=3):
    """Find relevant chunks using simple keyword matching."""

    query_words = set(
        query.lower().split()
    )

    scored_chunks = []

    for chunk in chunks:

        chunk_words = set(
            chunk.lower().split()
        )

        score = len(
            query_words.intersection(chunk_words)
        )

        scored_chunks.append(
            (score, chunk)
        )

    scored_chunks.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        chunk
        for score, chunk in scored_chunks[:top_k]
        if score > 0
    ]