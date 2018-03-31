import json

from Db.DbConn import DbConn


class Db(object):
    db_main = None

    @staticmethod
    def init():
        data = json.load(open('server.json'))
        Db.db_main = data['db']['main']
        print('db info initialized')

    @staticmethod
    def Main():
        return DbConn(Db.db_main)
