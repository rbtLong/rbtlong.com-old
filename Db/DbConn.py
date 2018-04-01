import mysql.connector


class DbConn(object):

    inf = {}

    def __init__(self, db_inf):
        self.inf = db_inf

    def connect(self, cb):
        cnx = None

        try:
            cnx = mysql.connector.MySQLConnection(
                user=self.inf['user'],
                password=self.inf['password'],
                host=self.inf['host'],
                database=self.inf['database'])
            return cb(cnx)

        finally:
            if cnx is not None:
                cnx.close()
            else:
                return None

    def rows(self, cb, cmd, params):
        def _m(cnx):
            curs = cnx.cursor(dictionary=True)
            curs.execute(cmd, params)

            results = []
            for row in curs:
                results.append(row)
            return cb(results)

        return self.connect(_m)
