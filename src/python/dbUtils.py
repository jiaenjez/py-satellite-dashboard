from src.python import appConfig, dbQueries, dbModel


def dbCommit():
    dbModel.db.session.commit()


def dbWrite(entryArray):
    for entry in entryArray:
        dbModel.db.session.add(entry)
    dbModel.db.session.commit()


def dbRead(queryName, *args):
    dbCursor = appConfig.dbConnection.cursor()
    if args:
        dbCursor.execute(dbQueries.queries[queryName](args))
    else:
        dbCursor.execute(dbQueries.queries[queryName])
    return dbCursor.fetchall()


def dbDropTable(tableName):
    dbCursor = appConfig.dbConnection.cursor()
    dbCursor.execute(dbQueries.queries["drop_table_by_name"](tableName))


def dbClose():
    dbModel.db.close_all_sessions()


def dbDropAll():
    dbModel.db.drop_all()


def dbCreateAll():
    dbModel.db.create_all()
