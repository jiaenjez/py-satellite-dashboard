/* eslint-disable */
import React, {useState} from 'react';
import {compose, withProps} from 'recompose';
import {
  withScriptjs, withGoogleMap, GoogleMap, Marker
} from 'react-google-maps';
import _ from 'lodash';
import {getPrediction, passPrediction} from './Utils';
import Select from '@mui/material/Select';
import {FormControl, InputLabel, MenuItem} from '@mui/material';

const API_KEY = process.env.REACT_APP_GOOGLE_MAP_API_KEY;

const Map = () => {
  const [cursorLatLng, setCursorLatLng] = useState({lat: 33.6405,
    lng: -117.8443});
  const [upcomingPass, setUpcomingPass] = useState({});
  const [dropdownSelect, setDropdownSelected] = useState('0 AMICALSAT');
  const [satelliteList, setSatelliteList] =
      useState(['0 NEXUS', '0 DIWATA 2B', '0 SIMPL',
        '0 E-STAR-2', 'LILACSAT-2', '0 SPROUT', '0 CUBEBUG 1',
        '0 OSCAR 11 (UoSAT 2)', '0 PSLV R/B', '0 CHUBUSAT 3',
        '0 EXOCUBE', 'SWISSCUBE', '0 KKS-1 (KISEKI)',
        '0 PRISM (HITOMI)', '0 EYESAT A', 'CHOMPTT',
        'ASTROCAST 0.1', 'S-NET D', '0 S-NET C', 'S-NET B',
        'S-NET A', 'ROBUSTA-1B', 'CUTE-1.7+APD II (CO-65)',
        '0 CUBESAT XI 5', '0 CUBESAT XI 4', 'CUTE-1 (CO-55)',
        'PCSAT (NO-44)', '0 AMICALSAT', 'ORIGAMISAT-1',
        '0 COMPASS 1', '0 HORYU 4', '0 CHUBUSAT 2', 'TRITON-1',
        'LAPAN-A2', 'SEEDS II (CO-66)', 'PSAT2 (NO-104)',
        '0 BRICSAT 2', '0 SALSAT', '0 CAPE-3', '0 YUSAT-1',
        '0 HIROGARI (OPUSAT II)', 'TSURU', 'MAYA-2',
        'GUARANISAT-1', 'MAYA-3', 'MAYA-4']);

  const handleSelectorChange = (event) => {
    setDropdownSelected(event.target.value);
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
        setCursorLatLng({lat: mouseEvent.latLng.lat(),
          lng: mouseEvent.latLng.lng()});
        getPrediction(cursorLatLng);
        setUpcomingPass(passPrediction);
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
        autoWidth={true}
        autoComplete={true}
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
