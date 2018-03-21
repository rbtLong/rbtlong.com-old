import json
import mysql.connector

from flask import Flask

from Core import corebp

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

    try:
        print("Parsing Server.json")
        data = json.load(open('server.json'))
        host = data['host']
        port = data['port']
        env = data['env']
        db_main = data['db']['main']

        try:
            db_main_test(db_main)
        except ConnectionError as dberr:
            print(f"[db_main] Failed to connect: {dberr}")

        debug = env == 'prod'
        print(f"running on host={host} port={port} debug={debug}")
        app.register_blueprint(corebp)
        app.run(host=host, port=port, debug=debug)

    except IOError as e:
        print(f"Error: {e.errno} {e.strerror}")
