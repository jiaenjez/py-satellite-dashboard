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


@app.route('/flight_horizon', methods=['GET'])
def getHorizon():
    data = tle.loadTLE()["ISS (ZARYA)"]
    return flask.jsonify(calculation.getSerializedHorizon(calculation.findHorizonTime(data, 3 * 24 * 3600,
                                                                                      wgs84.latlon(33.643831,
                                                                                                   -117.841132,
                                                                                                   elevation_m=17))))


if __name__ == '__main__':
    print("logging: Running on http://127.0.0.1:5000/response")
    print("logging: Running on http://127.0.0.1:5000/tle")
    print("logging: Running on http://127.0.0.1:5000/location")
    print("logging: Running on http://127.0.0.1:5000/flight_path")
    print("logging: Running on http://127.0.0.1:5000/flight_horizon")
    app.run(debug=True)
