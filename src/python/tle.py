import json
import subprocess
from sys import platform as _platform
from datetime import datetime
from src.python import satnogs, dbModel, dbUtils
from pymemcache.client import base
import appConfig
import ast

# config for memcache
client = base.Client(('localhost', 11211))


def getTLE() -> {dict}:
    tleList = satnogs.tleFilter(satnogs.sortMostRecent(satnogs.satelliteFilter(satnogs.getSatellites())))
    keys = [tle['tle0'] for tle in tleList]
    return dict(zip(keys, tleList))


def isRecent(timestamp) -> bool:
    if timestamp is None:
        return False

    if not type(timestamp) is datetime:
        lastTimestamp = datetime.strptime(timestamp.decode("utf-8"), '%Y-%m-%d %H:%M:%S.%f')
    else:
        lastTimestamp = timestamp
    currentTimestamp = datetime.now()
    return (currentTimestamp - lastTimestamp).days <= 1


def clearMemcache():
    # for Testing/Debug
    if not client.get("keySet") is None:
        keySet = ast.literal_eval((client.get("keySet")).decode("utf-8"))
        for key in keySet:
            client.set(key.replace(" ", "_"), None)

    client.set("currTime", None)
    client.set("keySet", None)
    client.flush_all()


def writeMemcache(data):
    currTime = datetime.now()
    client.set("currTime", currTime)
    keySet = set(data.keys())
    client.set("keySet", keySet)
    for key in keySet:
        client.set(key.replace(" ", "_"), data[key])


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
    keySet = ast.literal_eval((client.get("keySet")).decode("utf-8"))

    for key in keySet:
        value = client.get(key.replace(" ", "_")).decode("utf-8")  # byte -> str
        data[key] = ast.literal_eval(value)  # str -> dict
    return data


def writeDB(data):
    data = [dbModel.tle_create_row(key, data[key]['tle1'], data[key]['tle2'],
                                   datetime.now()) for key in data.keys()]
    print(data)
    dbUtils.dbWrite(data, force_refresh=True)


def readDB():
    if not appConfig.enableDB:
        return saveTLE()

    if not dbUtils.dbRead("get_tle_timestamp"):
        return saveTLE()

    timestamp, = dbUtils.dbRead("get_tle_timestamp")
    if not isRecent(timestamp):
        print("WARNING: db outdated")
        return saveTLE()

    dbData: dict = dbUtils.dbRead("find_tle_all", toDict=True)
    dbData = dbUtils.dbConvertDict(dbData)
    data = dict(zip([tle['tle0'] for tle in dbData], dbData))

    if data:
        writeMemcache(data)
        return data
    else:
        return saveTLE()


def saveTLE() -> {dict}:
    data = getTLE()

    if appConfig.enableMemcache:
        if _platform == "darwin":
            print("LOGGING: writing to cache")
            writeMemcache(data)

    if appConfig.enableDB:
        print("LOGGING: writing to db")
        writeDB(data)
        print("LOGGING: done writing to db")

    return data


def loadTLE() -> {dict}:
    if appConfig.enableMemcache:
        data = readMemcache()
        return data if data else readDB()
    else:
        return readDB()


appConfig.enableDB = False
clearMemcache()
print(loadTLE())
appConfig.enableDB = True
clearMemcache()
print(loadTLE())
clearMemcache()
print(loadTLE())
