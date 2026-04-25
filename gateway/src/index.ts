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
  console.log(`✅ Gateway listening on http://localhost:${PORT}`);
});