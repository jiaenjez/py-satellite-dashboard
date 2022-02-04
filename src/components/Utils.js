const getPrediction = (latLng, satellite) => {
  return fetch('/prediction', {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
      'accept': 'application/json'
    },
    body: JSON.stringify({rxLatLng: latLng,
      satellite: satellite})
  }).then((response) => {
    return response.json();
  }).then((data) => {
    return data;
  });
};

const getAvailableSatellite = () => {
  return fetch('/available_satellite', {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
      'accept': 'application/json'
    }
  }).then((response) => {
    return response.json();
  }).then((data) => {
    return data;
  });
};

export {getPrediction, getAvailableSatellite};
