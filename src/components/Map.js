/* eslint-disable */
import React, {useState} from 'react';
import {compose, withProps} from 'recompose';
import {
  withScriptjs, withGoogleMap, GoogleMap, Marker,
} from 'react-google-maps';

const API_KEY = process.env.REACT_APP_GOOGLE_MAP_API_KEY;

const Map = () => {
  const [marker, setMarker] = useState('');
  const defaultLocation = {lat: 33.6405, lng: -117.8443};

  const EmbeddedMap = compose(
      withProps({
        googleMapURL: `https://maps.googleapis.com/maps/api/js?key=${API_KEY}&v=3.exp&libraries=geometry,drawing,places`,
        loadingElement: <div style={{height: `100%`}} />,
        containerElement: <div style={{height: `400px`}} />,
        mapElement: <div style={{height: `100%`}} />,
        currentLocation: defaultLocation,
        isMarkerShown: true
      }),
      withScriptjs,
      withGoogleMap,
  )((props) => (
    <GoogleMap
      onClick={(mouseEvent) => {
        props.currentLocation.lat = mouseEvent.latLng.lat();
        props.currentLocation.lng = mouseEvent.latLng.lng();
        setMarker(`${mouseEvent.latLng.lat()}, ${mouseEvent.latLng.lng()}`);
      }}
      defaultZoom={7}
      defaultCenter={defaultLocation}
    >
      {props.isMarkerShown && (
        <Marker
          position={props.currentLocation}
        />
      )}
    </GoogleMap>
  ));

  return <div className="Map">
    <EmbeddedMap />
    <p className="Marker">pointer location: {marker}</p>
  </div>;
};

export default Map;
/* eslint-enable */
