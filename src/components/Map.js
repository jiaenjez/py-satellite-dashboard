import React from 'react'
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const mapStyle = {
    width: '400px',
    height: '400px'
};

const uc_irvine = {lat:33.6405 ,lng:-117.8443}

function MyComponent() {
    return (
        <LoadScript
            googleMapsApiKey="AIzaSyC3eh-avwD6U3CGDh6DjKuoCcGN9J1b8EA"
        >
            <GoogleMap
                mapContainerStyle={mapStyle}
                center={uc_irvine}
                zoom={10}
            >
                { /* add more Child components: markers, info windows*/
                    <Marker
                        position={{ lat: 33.6405, lng: -117.8443 }}
                    />
                }
                <></>
            </GoogleMap>
        </LoadScript>
    )
}

export default React.memo(MyComponent)

