import subprocess
from sys import platform as _platform
from datetime import datetime
from src.python import satnogs, dbModel, dbUtils
from pymemcache.client import base
from appConfig import db
import ast

# config for memcache
client = base.Client(('localhost', 11211))


def getTLE() -> {dict}:  # {tle["tle0"]: tle for tle in requests.get(TLE_URL).json()}
    tleList = satnogs.tleFilter(satnogs.sortMostRecent(satnogs.satelliteFilter(satnogs.getSatellites())))
    keys = [tle['tle0'] for tle in tleList]
    return dict(zip(keys, tleList))


def writeMemcache(data):
    currTime = datetime.now()
    client.set("currTime", currTime)
    client.set("keySet", data.keys())
    for key in data.keys():
        cacheKey = key.replace(" ", "_")
        line = data[key]  # line = TLE info
        client.set(cacheKey, line)


def writeDB(data):
    dbUtils.dbDropAll()
    dbUtils.dbCreateAll()
    dbUtils.dbWrite([dbModel.tle_create_row(key, data[key]['tle1'], data[key]['tle2'],
                                            datetime.now()) for key in data.keys()])


def readDB():
    return dbUtils.dbRead("find_tle_all")


def readMemcache():
    try:
        timeStamp = client.get("currTime")
    except ConnectionRefusedError:
        timeStamp = None
        subprocess.run(["brew", "services", "stop", "memcached"])
        subprocess.run(["brew", "install", "memcached"])
        subprocess.run(["brew", "services", "start", "memcached"])

    if timeStamp is None:
        print("WARNING: cache miss")
        data = saveTLE()
        return data

    dateTimeObj = datetime.strptime(timeStamp.decode("utf-8"), '%Y-%m-%d %H:%M:%S.%f')
    newCurrTime = datetime.now()
    if (newCurrTime - dateTimeObj).days >= 1:
        print("WARNING: cache outdated")
        data = saveTLE()
        return data

    print("LOGGING: cache hit")
    data = dict()
    keySetString = (client.get("keySet")).decode("utf-8")
    keySet = ast.literal_eval(keySetString[10:-1])

    for k in keySet:
        key = k.replace(" ", "_")
        v = client.get(key).decode("utf-8")  # byte -> str
        data[k] = ast.literal_eval(v)  # str -> dict
    return data


def saveTLE() -> {dict}:
    data = getTLE()
    if _platform == "darwin":
        writeMemcache(data)
    writeDB(data)

    return data


def loadTLE() -> {dict}:
    if _platform != "darwin":
        return getTLE()

    return readMemcache()


def saveToDB():
    response = loadTLE()
    dbUtils.dbDropAll()
    dbUtils.dbCreateAll()
    dbUtils.dbWrite([dbModel.tle_create_row(key, response[key]['tle1'], response[key]['tle2'],
                                            datetime.now()) for key in response.keys()])

