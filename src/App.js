import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [location, setLocation] = useState(0);

  useEffect(() => {
    fetch('/location').then(res => res.json()).then(data => {
      setLocation([data.lat, ", " , data.long]);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />

        ... THIS IS JUST A DEMO OF REACT ...

        <p>UC Irvine is at {location}.</p>
      </header>
    </div>
  );
}

export default App;