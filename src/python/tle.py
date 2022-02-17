import json
import subprocess
from sys import platform as _platform
from datetime import datetime
from src.python import satnogs, dbModel, dbUtils
from pymemcache.client import base
from appConfig import db
import ast

# config for memcache
client = base.Client(('localhost', 11211))


def getTLE() -> {dict}:
    tleList = satnogs.tleFilter(satnogs.sortMostRecent(satnogs.satelliteFilter(satnogs.getSatellites())))
    keys = [tle['tle0'] for tle in tleList]
    return dict(zip(keys, tleList))


def clearMemcache():
    try:
        keySet = ast.literal_eval((client.get("keySet")).decode("utf-8")[10:-1])
    except AttributeError:
        pass
    else:
        for key in keySet:
            client.set(key.replace(" ", "_"), None)
    client.set("currTime", None)
    client.set("keySet", None)
    client.flush_all()


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
    if not dbUtils.dbRead("get_tle_timestamp"):
        return saveTLE()

    timestamp, = dbUtils.dbRead("get_tle_timestamp")
    print(isRecent(timestamp))
    if not isRecent(timestamp):
        return saveTLE()

    return dbUtils.dbRead("find_tle_all") if dbUtils.dbRead("find_tle_all") else saveTLE()


def readMemcache():
    try:
        timestamp = client.get("currTime")
    except ConnectionRefusedError:
        timestamp = None
        subprocess.run(["brew", "services", "stop", "memcached"])
        subprocess.run(["brew", "install", "memcached"])
        subprocess.run(["brew", "services", "start", "memcached"])

    if timestamp is None:
        print("WARNING: cache miss")
        return None

    if not isRecent(timestamp):
        print("WARNING: cache outdated")
        return None

    print("LOGGING: cache hit")
    data = dict()
    keySet = ast.literal_eval((client.get("keySet")).decode("utf-8")[10:-1])

    for key in keySet:
        value = client.get(key.replace(" ", "_")).decode("utf-8")  # byte -> str
        data[key] = ast.literal_eval(value)  # str -> dict
    return data


def saveTLE() -> {dict}:
    data = getTLE()
    if _platform == "darwin":
        writeMemcache(data)
    writeDB(data)

    return data


def loadTLE() -> {dict}:
    return readMemcache() if readMemcache() else readDB()


def isRecent(timestamp) -> bool:
    try:
        lastTimestamp = datetime.strptime(timestamp.decode("utf-8"), '%Y-%m-%d %H:%M:%S.%f')
    except AttributeError:
        lastTimestamp = timestamp
    currentTimestamp = datetime.now()
    return (currentTimestamp - lastTimestamp).days >= 1


# clearMemcache()
# print(saveTLE())

