import React from 'react';
import Time from './components/Time';
import Logo from './components/Logo';
import Map from './components/Map';
// import Location from './components/Location';
import './App.css';

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <Time />
        <Logo />
        <Map />
        {/* <Location />*/}
      </header>
    </div>
  );
};

export default App;
