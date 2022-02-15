from src.python import appConfig, dbQueries

dbCursor = appConfig.dbConnection.cursor()
dbCursor.execute(dbQueries.TLE_FIND_ISS)
for r in dbCursor.fetchall():
    print(r)
