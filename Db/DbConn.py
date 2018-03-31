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

            cb(cnx)

        except ConnectionError as dberr:
            print(f"[Core] Failed to connect: {dberr}")

        finally:
            if cnx is not None:
                cnx.close()

    @staticmethod
    def rows(cb, cmd, params):
        def _m(cnx):
            curs = cnx.cursor(dictionary=True)
            curs.execute(cmd, params)

            results = []
            for row in curs:
                results.append(row)
            cb(results)

        return Db.connect(_m)
