import json

from flask import Flask, send_from_directory, render_template

app = Flask(__name__)


@app.route('/api/<string:var1>')
def hello_world1(var1):
    return f'Hello {var1} !'


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if path == '' or path == '/':
        return send_from_directory('ui', 'index.html')
    else:
        return send_from_directory('ui', path)


if __name__ == '__main__':
    try:
        data = json.load(open('server.json'))
        host = data['host']
        port = data['port']
        env = data['env']

        debug = env == 'prod'
        print(f"running on host={host} port={port} debug={debug}")
        app.run(host=host, port=port, debug=debug)

    except IOError as e:
        print(f"Error: {e.errno} {e.strerror}")
