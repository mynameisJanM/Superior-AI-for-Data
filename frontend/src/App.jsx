import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [content, setContent] = useState('');
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

  const ingest = async () => {
    try {
      await axios.post(`${API_BASE}/api/ingest`, { content });
      alert('Ingest successful');
    } catch (error) {
      alert('Ingest error: ' + error.message);
    }
  };

  const search = async () => {
    try {
      const res = await axios.post(`${API_BASE}/api/query', { text: query });
      setResults(res.data.matches);
    } catch (error) {
      alert('Search error: ' + error.message);
    }
  };

  return (
    <div>
      <h1>Simple Continual AI</h1>
      <input value={content} onChange={e => setContent(e.target.value)} placeholder="Enter content to ingest" />
      <button onClick={ingest}>Ingest</button>
      <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Enter query to search" />
      <button onClick={search}>Query</button>
      <ul>
        {results.map(r => <li key={r.id}>{r.score}: {r.metadata?.content || 'No metadata'}</li>)}
      </ul>
    </div>
  );
};

export default App;