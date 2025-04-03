import React, { useState, useEffect } from 'react';

function App() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState('');

  useEffect(() => {
    fetch('http://backend-service:8000/items/')
      .then(res => res.json())
      .then(data => setItems(data));
  }, []);

  const addItem = () => {
    fetch('http://backend-service:8000/items/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name }),
    })
      .then(res => res.json())
      .then(data => setItems([...items, data]));
    setName('');
  };

  return (
    <div>
      <h1>Items</h1>
      <input value={name} onChange={e => setName(e.target.value)} />
      <button onClick={addItem}>Add Item</button>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;