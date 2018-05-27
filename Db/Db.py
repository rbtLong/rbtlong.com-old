import json

import mysql.connector

from Db.DbConn import DbConn


class Db(object):
    db_main = None

    @staticmethod
    def db_main_test(db_main):
        cnx = mysql.connector.MySQLConnection(user=db_main['user'],
                                              password=db_main['password'],
                                              host=db_main['host'],
                                              database=db_main['database'])
        cnx.ping()
        cnx.close()
        print("[db_main] Connection established.")

    @staticmethod
    def init():
        try:
            data = json.load(open('server.json'))
            Db.db_main = data['db']['main']
            print('[Db Config Main] db info initialized')

            Db.db_main_test(Db.db_main)

        except ConnectionError as e:
            print(f'[Db Config Main] Error {e.errno} {e.strerror}')
            raise

    @staticmethod
    def Main():
        return DbConn(Db.db_main)
