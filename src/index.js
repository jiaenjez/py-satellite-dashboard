import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import Location from './components/Location';
import Map from './components/Map';
import Time from './components/Time';
import Logo from './components/Logo';

ReactDOM.render(
    <React.StrictMode>
      <Location />
      <Map />
      <Time />
      <Logo />
    </React.StrictMode>,
    document.getElementById('root'),
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
