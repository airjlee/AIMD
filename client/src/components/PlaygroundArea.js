import React, { useState } from 'react';
import ResultDisplay from './ResultDisplay';

function PlaygroundArea() {
  const [prompt, setPrompt] = useState('');
  const [results, setResults] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("yo");
    try {
      const response = await fetch("http://localhost:8080/api/plan", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({prompt})
      })

      if (!response.ok) {
        throw new Error("not ok");
      }

      const data = await response.json();
      setResults(prompt);

    } catch (error) {
      console.error("error: ", error);
    }
  };

  return (
    <div className="playground">
      <p>Try out AIMD</p>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={prompt} 
          onChange={(e) => setPrompt(e.target.value)} 
          placeholder="Enter a symptom, condition, etc..." 
        />
        <button type="submit">Run</button>
      </form>
      <div className="results-area">
        {results.map((result, index) => (
          <ResultDisplay key={index} data={results} />
        ))}
      </div>
    </div>
  );
}

export default PlaygroundArea;