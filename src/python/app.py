import flask
import requests
from flask import Flask, request
from skyfield.toposlib import wgs84
from src.python import tle, geocoding, satnogs, calculation

app = Flask(__name__)


@app.route('/response', methods=['GET'])
def getResponse():
    return flask.jsonify(requests.get(satnogs.TLE_URL).json())


@app.route('/tle', methods=['GET'])
def getPayload():
    return flask.jsonify(tle.loadTLE())


@app.route('/location', methods=['POST'])
def getLatLong():
    addressLine = request.get_json().get('address')
    city = request.get_json().get('city')
    postalCode = request.get_json().get('postalCode')
    country = request.get_json().get('country')
    adminDistrict = request.get_json().get('adminDistrict')

    return flask.jsonify(geocoding.getLatLong(addressLine, city, adminDistrict, postalCode, country)[0])


@app.route('/flight_path', methods=['GET'])
def getCalculation():
    data = tle.getTLE()["ISS (ZARYA)"]
    return flask.jsonify(calculation.getSerializedPath(calculation.getPath(data, "latlong")))


@app.route('/flight_horizon', methods=['POST'])
def getHorizon():
    data = tle.loadTLE()
    selectedSatellite = data[list(data.keys())[0]]
    rxLatLng = request.get_json().get('rxLatLng').split(',')
    rxLat = float(rxLatLng[0])
    rxLong = float(rxLatLng[1])
    rxElevation = 0
    predictionDuration = 3 * 24 * 3600

    predictedPass = calculation.getSerializedHorizon(calculation.findHorizonTime(selectedSatellite, predictionDuration,
                                                                                 wgs84.latlon(rxLat, rxLong,
                                                                                              elevation_m=rxElevation)))

    return flask.jsonify(predictedPass)


if __name__ == '__main__':
    app.run(debug=True)
