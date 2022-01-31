import React from 'react';
import './App.css';
import Time from './components/Time';
import Logo from './components/Logo';
import Location from './components/Location';
import Map from './components/Map';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <Location />
        <Map />
        <Time />
        <Logo />
      </header>
    </div>
  );
};

export default App;
