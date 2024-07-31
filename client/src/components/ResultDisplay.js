import React from 'react';

function ResultDisplay({ data }) {
  return (
    <div className="result-card">
      <div className="result-tabs">
        <button>Markdown</button>
        <button>JSON response</button>
      </div>
      <p>{data.content}</p> {/* Render content as plain text */}
    </div>
  );
}

export default ResultDisplay;


