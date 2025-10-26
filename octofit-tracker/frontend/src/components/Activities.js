import React, { useEffect, useState } from 'react';

function renderTable(data) {
  if (!Array.isArray(data) || data.length === 0) {
    return <div className="p-3">No data available</div>;
  }

  const headers = Object.keys(data[0]);

  return (
    <div className="table-responsive">
      <table className="table table-striped table-hover data-table mb-0">
        <thead>
          <tr>
            {headers.map((h) => (
              <th key={h}>{h}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, idx) => (
            <tr key={idx}>
              {headers.map((h) => (
                <td key={h}>{typeof row[h] === 'object' ? JSON.stringify(row[h]) : String(row[h])}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default function Activities() {
  const [data, setData] = useState([]);
  const endpoint = process.env.REACT_APP_CODESPACE_NAME
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities`
    : `http://localhost:8000/api/activities`;

  const fetchData = () => {
    console.log('[Activities] endpoint ->', endpoint);
    fetch(endpoint)
      .then((res) => res.json())
      .then((json) => {
        console.log('[Activities] fetched ->', json);
        const payload = Array.isArray(json) ? json : json.results ?? json;
        setData(payload);
      })
      .catch((err) => console.error('[Activities] fetch error', err));
  };

  useEffect(() => {
    fetchData();
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <div className="card table-card">
        <div className="card-body">
          <div className="d-flex align-items-center justify-content-between mb-3">
            <h2 className="h5 mb-0">Activities</h2>
            <div>
              <button className="btn btn-outline-primary btn-sm" onClick={fetchData}>Refresh</button>
            </div>
          </div>
          {renderTable(data)}
        </div>
      </div>
    </div>
  );
}
