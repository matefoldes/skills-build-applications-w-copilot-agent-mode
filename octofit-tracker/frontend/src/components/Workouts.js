import React, { useEffect, useState } from 'react';

const resource = 'workouts';

export default function Workouts() {
  const [data, setData] = useState([]);
  const baseUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`;
  const endpoint = `${baseUrl}/${resource}/`;

  useEffect(() => {
    console.log('[Workouts] endpoint ->', endpoint);
    fetch(endpoint)
      .then((res) => res.json())
      .then((json) => {
        console.log('[Workouts] fetched ->', json);
        const payload = Array.isArray(json) ? json : json.results ?? json;
        setData(payload);
      })
      .catch((err) => console.error('[Workouts] fetch error', err));
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2>Workouts</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
