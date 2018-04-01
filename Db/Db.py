import json

from Db.DbConn import DbConn


class Db(object):
    db_main = None

    @staticmethod
    def init():
        try:
            data = json.load(open('server.json'))
            Db.db_main = data['db']['main']
            print('[Db Config Main] db info initialized')

        except ConnectionError as e:
            print(f'[Db Config Main] Error {e.errno} {e.strerror}')
            raise

    @staticmethod
    def Main():
        return DbConn(Db.db_main)
