from fastapi import FastAPI

app = FastAPI(title="DocChat RAG Service")


@app.get("/")
def root():
    return {"service": "rag-service", "status": "ok"}


@app.get("/health")
def health():
    return {"status": "healthy"}