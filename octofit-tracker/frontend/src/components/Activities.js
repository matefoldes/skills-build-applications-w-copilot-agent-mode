import React, { useEffect, useState } from 'react';

const resource = 'activities';

export default function Activities() {
  const [data, setData] = useState([]);
  const baseUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api`;
  const endpoint = `${baseUrl}/${resource}/`;

  useEffect(() => {
    console.log('[Activities] endpoint ->', endpoint);
    fetch(endpoint)
      .then((res) => res.json())
      .then((json) => {
        console.log('[Activities] fetched ->', json);
        const payload = Array.isArray(json) ? json : json.results ?? json;
        setData(payload);
      })
      .catch((err) => console.error('[Activities] fetch error', err));
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2>Activities</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
