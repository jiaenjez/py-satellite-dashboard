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
    data = tle.loadTLE()['0 AMICALSAT']
    return flask.jsonify(calculation.getSerializedPath(calculation.getPath(data, "latlong")))


@app.route('/available_satellite', methods=['GET'])
def getSatellite():
    return flask.jsonify(list(tle.loadTLE().keys()))


@app.route('/flight_horizon', methods=['POST'])
def getHorizon():
    selectedSatellite = request.get_json().get('satellite')
    rxLatLng = request.get_json().get('rxLatLng')
    rxLat = rxLatLng['lat']
    rxLong = rxLatLng['lng']
    rxElevation = 0
    predictionDuration = 1 * 24 * 3600

    predictedPass = calculation.findHorizonTime(tle.loadTLE()[selectedSatellite], predictionDuration,
                                                wgs84.latlon(rxLat, rxLong,
                                                             elevation_m=rxElevation))

    return predictedPass


if __name__ == '__main__':
    app.run(debug=True)
