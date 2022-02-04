let passPrediction = null;
let availableSatellite = null;

const getPrediction = (latLng, satellite) => {
  fetch('/flight_horizon', {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
      'accept': 'application/json'
    },
    body: JSON.stringify({rxLatLng: latLng,
      satellite: satellite})
  }).then((response) => response.json()).then((data) => {
    alert('Request Success');
    passPrediction = data;
  });
};

const getAvailableSatellite = () => {
  fetch('/available_satellite', {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
      'accept': 'application/json'
    }
  }).then((response) => response.json()).then((data) => {
    availableSatellite = data;
  });
};

export {getPrediction, passPrediction,
  getAvailableSatellite, availableSatellite
};
