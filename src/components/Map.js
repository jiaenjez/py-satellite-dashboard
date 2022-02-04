/* eslint-disable */
import React, {useState} from 'react';
import {compose, withProps} from 'recompose';
import {
  withScriptjs, withGoogleMap, GoogleMap, Marker
} from 'react-google-maps';
// import {getPrediction, formatPrediction} from './Utils';


const _ = require('lodash');
const API_KEY = process.env.REACT_APP_GOOGLE_MAP_API_KEY;

const Map = () => {
  const [cursorLatLng, setCursorLatLng] = useState({lat: 33.6405,
    lng: -117.8443});
  const [upcomingPass, setUpcomingPass] = useState({});

  const EmbeddedMap = compose(
      withProps({
        googleMapURL: `https://maps.googleapis.com/maps/api/js?key=${API_KEY}&v=3.exp&libraries=geometry,drawing,places`,
        loadingElement: <div style={{height: `100%`}} />,
        containerElement: <div style={{height: `400px`}} />,
        mapElement: <div style={{height: `100%`}} />
      }),
      withScriptjs,
      withGoogleMap
  )(() => (
    <GoogleMap
      defaultZoom={7}
      defaultCenter={cursorLatLng}
      onClick={(mouseEvent) => {
        setCursorLatLng(`${mouseEvent.latLng.lat()},${mouseEvent.latLng.lng()}`);
        fetch('/flight_horizon', {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
            'accept': 'application/json'
          },
          body: JSON.stringify({rxLatLng: cursorLatLng})
        }).then((response) => response.json()).then((data) => {
          alert('Request Success');
          setUpcomingPass(data);
        });
      }}
    >
      {(<Marker position={cursorLatLng} />
      )}
    </GoogleMap>
  ));

  return <div className="Map">
    <EmbeddedMap />
    <p className="Marker">Cursor location: {`Latitude: ${cursorLatLng.lat} Longitude: ${cursorLatLng.lng}`}</p>
    <p className="Pass">Upcoming pass: </p>
    <ol>
      {_.map(upcomingPass, (k, v) => (
        <li>{v}: {k}</li>
      ))}
    </ol>
  </div>;
};

export default Map;
/* eslint-enable */
