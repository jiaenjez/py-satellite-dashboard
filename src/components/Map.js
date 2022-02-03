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
  const [marker, setMarker] = useState('');
  const [info, setInfo] = useState('');
  const defaultLocation = {lat: 33.6405, lng: -117.8443};

  const EmbeddedMap = compose(
      withProps({
        googleMapURL: `https://maps.googleapis.com/maps/api/js?key=${API_KEY}&v=3.exp&libraries=geometry,drawing,places`,
        loadingElement: <div style={{height: `100%`}} />,
        containerElement: <div style={{height: `400px`}} />,
        mapElement: <div style={{height: `100%`}} />
      }),
      withScriptjs,
      withGoogleMap
  )((props) => (
    <GoogleMap
      defaultZoom={7}
      defaultCenter={defaultLocation}
      onClick={(mouseEvent) => {
        setMarker(`${mouseEvent.latLng.lat()},${mouseEvent.latLng.lng()}`);
        fetch('/flight_horizon', {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json',
            'accept': 'application/json'
          },
          body: JSON.stringify({rxLatLng: marker})
        }).then((response) => response.json()).then((data) => {
          alert('Request Success');
          setInfo(JSON.stringify(data));
        });
      }}
    >
      {(<Marker position={{lat: marker.lat, lng: marker.lng}} />
      )}
    </GoogleMap>
  ));

  return <div className="Map">
    <EmbeddedMap />
    <p className="Marker">Cursor location: {marker}</p>
    <p className="Marker">Upcoming pass: {info}</p>
  </div>;
};

export default Map;
/* eslint-enable */
