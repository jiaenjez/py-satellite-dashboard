import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

// this is just a example, we should really consider using https://formik.org/docs/overview

function App() {
  const [location, setLocation] = useState(0);
  const [addr, setAddr] = useState("")

  const handleChange = event => {
    setAddr(event.target.value)
    console.log(event.target.value)  // right click -> inspect -> console
  }

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
        <p></p>

        <form>
          <label>
            Address: <input type="text" value={addr} onChange={handleChange} size="60"/>
          </label>
        </form>

        <p>UC Irvine is at {location}.</p>
      </header>
    </div>
  );
}

export default App;