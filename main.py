import json

import mysql.connector
from flask import Flask

from Core import corebp
from Db.Db import Db

app = Flask(__name__)


def db_main_test(db_main):
    cnx = mysql.connector.MySQLConnection(user=db_main['user'],
                                          password=db_main['password'],
                                          host=db_main['host'],
                                          database=db_main['database'])
    cnx.ping()
    cnx.close()
    print("[db_main] Connection established.")


if __name__ == '__main__':

    Db.init()

    try:
        data = json.load(open('server.json'))
        host = data['host']
        port = data['port']
        env = data['env']
        print(f'[App Config] app config parsed')

        debug = env == 'prod'
        print(f"running on host={host} port={port} debug={debug}")

        app.register_blueprint(corebp)
        app.run(host=host, port=port, debug=debug)

    except IOError as e:
        print(f"[Config] Error: {e.errno} {e.strerror}")


