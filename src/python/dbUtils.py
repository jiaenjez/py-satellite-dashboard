import psycopg2
import psycopg2.extras
from sqlalchemy import exc

import appConfig
import dbModel
import dbQueries


def dbCommit():
    dbModel.db.session.commit()


def dbWrite(entryArray, **kwargs):
    if 'force_refresh' in kwargs.keys() and kwargs['force_refresh']:
        # dbModel.db.drop_all()
        # dbModel.db.create_all()
        pass
    for entry in entryArray:
        dbModel.db.session.add(entry)

    try:
        dbModel.db.session.commit()
    except exc.ProgrammingError:
        dbModel.db.create_all()
        for entry in entryArray:
            dbModel.db.session.add(entry)
        dbModel.db.session.commit()
    dbModel.db.session.commit()


def dbRead(queryName, *args, **kwargs):
    """

    :param queryName: list of query inside dbQueries.py
    :param args: pass parameter into SQL query
    :param kwargs: return a dict-like object if dict=true, else return a list of tuple
    :return:
    """
    if 'dict' in kwargs.keys() and kwargs['dict']:
        dbCursor = appConfig.dbConnection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    else:
        dbCursor = appConfig.dbConnection.cursor()
    try:
        if args:
            dbCursor.execute(dbQueries.queries[queryName](args))
        else:
            dbCursor.execute(dbQueries.queries[queryName]())
    except psycopg2.errors.UndefinedTable:
        return None

    dbResponse: [()] = dbCursor.fetchall()
    return None if len(dbResponse) == 0 else dbResponse[0] if len(dbResponse) == 1 else dbResponse


def dbDropTable(tableName):
    dbCursor = appConfig.dbConnection.cursor()
    dbCursor.execute(dbQueries.queries["drop_table_by_name"](tableName))


def dbClose():
    dbModel.db.close_all_sessions()


def dbDropAll():
    dbModel.db.drop_all()


def dbCreateAll():
    dbModel.db.create_all()
