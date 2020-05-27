import mysql.connector


class UseDatabase:

    def __init__(self, dbconf):
        self.dbconf = dbconf

    def __enter__(self):
        self.conn = mysql.connector.connect(**self.dbconf)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
