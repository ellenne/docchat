from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_pages(pages: list[dict]) -> list[dict]:
    """
    Split pages into chunks of ~800 characters with 100 char overlap.
    Each chunk preserves its source page number for citation.

    Returns: [{"text": "...", "page": 3}, ...]
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    all_chunks = []
    for page in pages:
        chunks = splitter.split_text(page["text"])
        for chunk in chunks:
            all_chunks.append({"text": chunk, "page": page["page"]})

    return all_chunks