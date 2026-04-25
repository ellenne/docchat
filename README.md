# DocChat

A full-stack RAG (Retrieval-Augmented Generation) application: upload a PDF, ask questions about it, get answers with citations.

> 🚧 **Work in progress.** Built as a portfolio project to demonstrate end-to-end AI engineering — from data ingestion through embedding, retrieval, and LLM generation, with a TypeScript frontend and Node gateway in front of a Python ML service.

## Architecture

Three services, deployed independently:

| Service | Stack | Port | Role |
|---|---|---|---|
| `frontend/` | React + TypeScript + Vite | 5173 | UI: PDF upload, chat, citations |
| `gateway/` | Node + Express + TypeScript | 3001 | API gateway, request routing |
| `rag-service/` | Python + FastAPI | 8000 | Chunking, embedding, retrieval, LLM calls |

## Tech stack

- **LLM:** Anthropic Claude (generation)
- **Embeddings:** OpenAI `text-embedding-3-small`
- **Vector store:** ChromaDB (local, persistent)
- **PDF parsing:** PyMuPDF
- **Chunking:** LangChain recursive character splitter

## Status

- [x] Service scaffolding (FastAPI, Express, React)
- [ ] PDF ingestion + chunking + embedding
- [ ] RAG query endpoint with Claude
- [ ] Streaming responses across the stack
- [ ] Citation rendering in the UI
- [ ] Agent mode with tool use

## Running locally

Each service runs independently. See its folder for setup instructions.

```bash
# rag-service
cd rag-service
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

```bash
# gateway
cd gateway
npm install
npm run dev
```

## Author

Luigi Neri — [LinkedIn](https://www.linkedin.com/in/luigineri82/)