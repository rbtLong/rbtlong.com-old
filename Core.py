import mysql.connector
from flask import send_from_directory, Blueprint, json, Response

corebp = Blueprint('profile', __name__)

@corebp.route('/', defaults={'path': ''})
@corebp.route('/<path:path>')
def index(path):
    if path == '' or path == '/':
        return send_from_directory('ui', 'index.html')
    else:
        return send_from_directory('ui', path)


@corebp.route('/api/skills')
def skills():
    try:
        data = json.load(open('server.json'))
        db_main = data['db']['main']

        try:
            cnx = mysql.connector.MySQLConnection(user=db_main['user'],
                                                  password=db_main['password'],
                                                  host=db_main['host'],
                                                  database=db_main['database'])
            curs = cnx.cursor(dictionary=True)
            curs.execute("select * from rbtlong.skills")
            results = []
            for row in curs:
                results.append(row)
            cnx.close()

            res = {
                "success": 1,
                "content": results
            }

            return Response(json.dumps(res), mimetype='application/json')

        except ConnectionError as dberr:
            res = {"success": 0, "reason": 'db conn'}
            print(f"[Core] Failed to connect: {dberr}")
            return Response(json.dumps(res), mimetype='application/json')

    except IOError as ioerr:
        res = {"success": 0, "reason": 'io err'}
        print(f"[Core] Failed to connect: {dberr}")
        return Response(json.dumps(res), mimetype='application/json')
