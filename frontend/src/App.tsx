import { useEffect, useState } from "react";

interface HealthResponse {
  service: string;
  status: string;
}

function App() {
  const [gatewayHealth, setGatewayHealth] = useState<HealthResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("http://localhost:3001/")
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data: HealthResponse) => setGatewayHealth(data))
      .catch((err: Error) => setError(err.message));
  }, []);

  return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center p-8">
      <div className="bg-white rounded-2xl shadow p-8 max-w-md w-full">
        <h1 className="text-2xl font-bold text-slate-800 mb-2">DocChat</h1>
        <p className="text-slate-500 mb-6">Frontend is alive 👋</p>

        <div className="border-t pt-4">
          <div className="text-sm text-slate-500 mb-1">Gateway connection</div>
          {gatewayHealth && (
            <div className="text-green-700 font-mono text-sm">
              ✅ {gatewayHealth.service} — {gatewayHealth.status}
            </div>
          )}
          {error && (
            <div className="text-red-700 font-mono text-sm">
              ❌ {error}
            </div>
          )}
          {!gatewayHealth && !error && (
            <div className="text-slate-400 text-sm">Connecting…</div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;