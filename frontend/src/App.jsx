import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [content, setContent] = useState('');
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

  const ingest = async () => {
    setLoading(true);
    setError('');
    try {
      await axios.post(`${API_BASE}/api/ingest`, { content });
      alert('Ingest successful');
      setContent('');
    } catch (err) {
      console.error("Ingest error:", err);
      setError('Ingest failed: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  const search = async () => {
    setLoading(true);
    setError('');
    try {
      const res = await axios.post(`${API_BASE}/api/query`, { text: query });
      setResults(res.data.matches || []);
    } catch (err) {
      console.error("Search error:", err);
      setError('Search failed: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="app">
      <h1>Simple Continual AI</h1>
      <div className="input-group">
        <input
          value={content}
          onChange={e => setContent(e.target.value)}
          placeholder="Enter content to ingest"
          className="input"
          disabled={loading}
        />
        <button onClick={ingest} disabled={loading} className="button">
          {loading ? 'Loading...' : 'Ingest'}
        </button>
      </div>
      <div className="input-group">
        <input
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="Enter query to search"
          className="input"
          disabled={loading}
        />
        <button onClick={search} disabled={loading} className="button">
          {loading ? 'Loading...' : 'Query'}
        </button>
      </div>
      <ul className="results">
        {results.map(r => (
          <li key={r.id}>
            Score: {r.score} - Content: {r.metadata?.content || 'No metadata'}
          </li>
        ))}
      </ul>
      {loading && <p className="loading">Loading...</p>}
    </div>
  );
};

export default App;