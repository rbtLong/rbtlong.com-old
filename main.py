import json

from flask import Flask

from Core import corebp
from Db.Db import Db

app = Flask(__name__)

if __name__ == '__main__':

    Db.init()

    try:
        data = json.load(open('server.json'))
        host = data['host']
        port = data['port']
        env = data['env']
        print(f'[App Config] app config parsed')

        debug = env != 'prod'
        print(f"running on host={host} port={port} debug={debug}")

        app.register_blueprint(corebp)
        app.run(host=host, port=port, debug=debug)

    except IOError as e:
        print(f"[Config] Error: {e.errno} {e.strerror}")


