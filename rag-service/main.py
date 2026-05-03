import os
import uuid
from fastapi import FastAPI, UploadFile, File, HTTPException
from dotenv import load_dotenv

# IMPORTANT: load_dotenv() must run BEFORE we import services that read env vars
load_dotenv()

from services.pdf_loader import extract_text_from_pdf
from services.chunker import chunk_pages
from services.vector_store import add_chunks

app = FastAPI(title="DocChat RAG Service")


@app.get("/")
def root():
    return {"service": "rag-service", "status": "ok"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "anthropic_key_loaded": bool(os.getenv("ANTHROPIC_API_KEY")),
        "openai_key_loaded": bool(os.getenv("OPENAI_API_KEY")),
    }


@app.post("/ingest")
async def ingest(file: UploadFile = File(...)):
    """
    Accept a PDF, extract text, chunk it, embed it, store it.
    Returns a doc_id used to query this document later.
    """
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File must be a PDF")

    pdf_bytes = await file.read()
    if len(pdf_bytes) == 0:
        raise HTTPException(status_code=400, detail="Empty file")

    try:
        pages = extract_text_from_pdf(pdf_bytes)
        if not pages:
            raise HTTPException(status_code=400, detail="No text found in PDF")

        chunks = chunk_pages(pages)
        doc_id = uuid.uuid4().hex[:12]
        n_chunks = add_chunks(doc_id, chunks)

        return {
            "doc_id": doc_id,
            "filename": file.filename,
            "pages": len(pages),
            "chunks": n_chunks,
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")