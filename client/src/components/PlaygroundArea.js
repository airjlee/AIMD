import React, { useState } from 'react';
import ResultDisplay from './ResultDisplay';

function PlaygroundArea() {
  const [url, setUrl] = useState('');
  const [results, setResults] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Call your backend API here
    // Update results state with the response
  };

  return (
    <div className="playground">
      <p>Try out AIMD</p>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={url} 
          onChange={(e) => setUrl(e.target.value)} 
          placeholder="Enter a symptom, condition, etc..." 
        />
        <button type="submit">Run</button>
      </form>
      <div className="results-area">
        {results.map((result, index) => (
          <ResultDisplay key={index} data={result} />
        ))}
      </div>
    </div>
  );
}

export default PlaygroundArea;