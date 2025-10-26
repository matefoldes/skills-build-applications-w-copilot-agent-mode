import React, { useEffect, useState } from 'react';

const resource = 'leaderboard';

export default function Leaderboard() {
  const [data, setData] = useState([]);
  const baseUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`;
  const endpoint = `${baseUrl}/${resource}/`;

  useEffect(() => {
    console.log('[Leaderboard] endpoint ->', endpoint);
    fetch(endpoint)
      .then((res) => res.json())
      .then((json) => {
        console.log('[Leaderboard] fetched ->', json);
        const payload = Array.isArray(json) ? json : json.results ?? json;
        setData(payload);
      })
      .catch((err) => console.error('[Leaderboard] fetch error', err));
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2>Leaderboard</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
