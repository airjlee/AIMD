import React from 'react';

function ResultDisplay({ data }) {
  return (
    <div className="result-card">
      <h3>{data.title}</h3>
      <div className="result-tabs">
        <button>Markdown</button>
        <button>JSON response</button>
      </div>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default ResultDisplay;