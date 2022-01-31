import React from 'react';
import './App.css';
import Time from './components/Time';
import Logo from './components/Logo';
import Location from './components/Location';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <Location />
        <Time />
        <Logo />
      </header>
    </div>
  );
};

export default App;
