import os
import chromadb
from chromadb.utils import embedding_functions

# Persistent ChromaDB at ./chroma_db (gitignored)
_client = chromadb.PersistentClient(path="./chroma_db")

# OpenAI embedding function — uses text-embedding-3-small
# (cheap, 1536 dimensions, good retrieval quality)
_embedding_fn = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-3-small",
)


def get_or_create_collection(doc_id: str):
    """One collection per uploaded document."""
    return _client.get_or_create_collection(
        name=f"doc_{doc_id}",
        embedding_function=_embedding_fn,
    )


def add_chunks(doc_id: str, chunks: list[dict]) -> int:
    """
    Embed and store chunks in ChromaDB.
    Returns the number of chunks added.
    """
    collection = get_or_create_collection(doc_id)
    collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"page": c["page"]} for c in chunks],
        ids=[f"{doc_id}_chunk_{i}" for i in range(len(chunks))],
    )
    return len(chunks)