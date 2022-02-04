/* eslint-disable */
import React, {useEffect, useState} from 'react';
import {compose, withProps} from 'recompose';
import {
  withScriptjs, withGoogleMap, GoogleMap, Marker
} from 'react-google-maps';
import _ from 'lodash';
import {getAvailableSatellite, getPrediction} from './Utils';
import Select from '@mui/material/Select';
import {FormControl, InputLabel, MenuItem} from '@mui/material';

const API_KEY = process.env.REACT_APP_GOOGLE_MAP_API_KEY;

const Map = () => {
  const [cursorLatLng, setCursorLatLng] =
      useState({lat: 33.6405, lng: -117.8443});
  const [upcomingPass, setUpcomingPass] =
      useState({});
  const [dropdownSelect, setDropdownSelected] =
      useState('');
  const [satelliteList, setSatelliteList] =
      useState([]);
  const [isInitialized, setIsInitialized] =
      useState(false);

  if (!isInitialized) {
    getAvailableSatellite().then((data) => {
      setSatelliteList(data);
    });
    setIsInitialized(true);
  }

  const handleSelectorChange = (event) => {
    setDropdownSelected(event.target.value);
    getPrediction(cursorLatLng, dropdownSelect).then((prediction) => {
      setUpcomingPass(prediction);
    });
  };

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
        setCursorLatLng({
          lat: mouseEvent.latLng.lat(),
          lng: mouseEvent.latLng.lng()
        });
        getPrediction(cursorLatLng, dropdownSelect).then((prediction) => {
          setUpcomingPass(prediction);
        });
      }}
    >
      {(<Marker position={cursorLatLng} />
      )}
    </GoogleMap>
  ));

  return <div className="Map">
    <EmbeddedMap />
    <FormControl sx={{m: 1, minWidth: 100}}>
      <InputLabel id="demo-simple-select-label" >Tracking Satellite</InputLabel>
      <Select
        labelId="satellite-selector"
        id="satellite-selector"
        value={dropdownSelect}
        label="Satellite"
        onChange={handleSelectorChange}
      >
        {_.map(_.range(satelliteList.length), (index) => (
          <MenuItem value={`${satelliteList[index]}`}>
            {`${satelliteList[index]}`}</MenuItem>
        ))}
      </Select>
    </FormControl>
    <p className="Marker">Cursor location:
      {`Latitude: ${cursorLatLng.lat} Longitude: ${cursorLatLng.lng}`}</p>
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
