let passPrediction = null;

const getPrediction = (latLng) => {
  fetch('/flight_horizon', {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
      'accept': 'application/json'
    },
    body: JSON.stringify({rxLatLng: latLng})
  }).then((response) => response.json()).then((data) => {
    alert('Request Success');
    passPrediction = data;
  });
};

export {getPrediction,
  passPrediction};
