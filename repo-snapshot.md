# Repo Snapshot
## Git state
  chore/initial-readme
* main
  setup/node-gateway
  remotes/origin/chore/initial-readme
  remotes/origin/main
  remotes/origin/setup/node-gateway
  remotes/origin/setup/rag-service-skeleton

## Recent commits
903183c (HEAD -> main, origin/main) Merge pull request #2 from ellenne/chore/initial-readme
b7c579a (origin/chore/initial-readme, chore/initial-readme) Add README.md for DocChat project, outlining architecture, tech stack, and local setup instructions.
04d8fd7 Merge pull request #1 from ellenne/setup/node-gateway
0bb226f (origin/setup/node-gateway, setup/node-gateway) Add Node Express gateway skeleton with health endpoint
005477a (origin/setup/rag-service-skeleton) Add FastAPI rag-service skeleton

## Folder structure (depth 3, ignoring noise)
(Get-ChildItem -Recurse -Depth 3 -Force | Where-Object { 
_.FullName -notmatch '\\(node_modules|\.venv|\.git|dist|build|pycache|chroma_db)\' } | Select-Object FullName | Format-Table -AutoSize | Out-String)
## File contents

### README.md
```markdown
# DocChat

A full-stack RAG (Retrieval-Augmented Generation) application: upload a PDF, ask questions about it, get answers with citations.

> ðŸš§ **Work in progress.** Built as a portfolio project to demonstrate end-to-end AI engineering â€” from data ingestion through embedding, retrieval, and LLM generation, with a TypeScript frontend and Node gateway in front of a Python ML service.

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

Luigi Neri â€” [LinkedIn](https://www.linkedin.com/in/luigineri82/)
```

### .gitignore
# Node
node_modules/
dist/
.env
.env.local
.env.*.local

# Python
.venv/
venv/
__pycache__/
*.pyc
.pytest_cache/
*.egg-info/

# Vector store data
chroma_db/
*.sqlite3

# IDE
.vscode/
.idea/
*.swp
.DS_Store

# Build / logs
build/
*.log
### rag-service/main.py
```python
from fastapi import FastAPI

app = FastAPI(title="DocChat RAG Service")


@app.get("/")
def root():
    return {"service": "rag-service", "status": "ok"}


@app.get("/health")
def health():
    return {"status": "healthy"}
```

### rag-service/requirements.txt
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.13.0
click==8.3.3
colorama==0.4.6
exceptiongroup==1.3.1
fastapi==0.136.1
h11==0.16.0
httptools==0.7.1
idna==3.13
pydantic==2.13.3
pydantic_core==2.46.3
python-dotenv==1.2.2
python-multipart==0.0.26
PyYAML==6.0.3
starlette==1.0.0
typing-inspection==0.4.2
typing_extensions==4.15.0
uvicorn==0.46.0
watchfiles==1.1.1
websockets==16.0

### gateway/package.json
```json
{
  "name": "gateway",
  "version": "1.0.0",
  "type": "module",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "cors": "^2.8.6",
    "dotenv": "^17.4.2",
    "express": "^5.2.1"
  },
  "devDependencies": {
    "@types/cors": "^2.8.19",
    "@types/express": "^5.0.6",
    "@types/node": "^25.6.0",
    "tsx": "^4.21.0",
    "typescript": "^6.0.3"
  }
}

```

### gateway/tsconfig.json
```json
{
    "compilerOptions": {
      "target": "ES2022",
      "module": "ESNext",
      "moduleResolution": "Bundler",
      "esModuleInterop": true,
      "forceConsistentCasingInFileNames": true,
      "strict": true,
      "skipLibCheck": true,
      "resolveJsonModule": true,
      "outDir": "dist",
      "rootDir": "src"
    },
    "include": ["src/**/*"],
    "exclude": ["node_modules", "dist"]
  }
```

### gateway/src/index.ts
```typescript
import express, { Request, Response } from "express";
import cors from "cors";
import "dotenv/config";

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.get("/", (_req: Request, res: Response) => {
  res.json({ service: "gateway", status: "ok" });
});

app.get("/health", (_req: Request, res: Response) => {
  res.json({ status: "healthy" });
});

// Start server
app.listen(PORT, () => {
  console.log(`âœ… Gateway listening on http://localhost:${PORT}`);
});
```

### frontend/package.json
```json
(does not exist - frontend not yet scaffolded)
```

### frontend/src/App.tsx
```typescript
(does not exist - frontend not yet scaffolded)
```

## Environment files (presence only - never paste contents)
(Get-ChildItem -Recurse -Force -Filter '.env*' -ErrorAction SilentlyContinue | Where-Object { 
_.FullName -notmatch '\\(node_modules|\.venv|\.git)\\' } | Select-Object FullName | Format-Table -AutoSize | Out-String)
