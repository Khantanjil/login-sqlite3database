import sqlite3


class Database():

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS account_credentials (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
        )
        self.conn.commit()

    def view(self):
        self.cur.execute(
            "SELECT * FROM account_credentials"
        )
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def insert(self, username, password):
        self.cur.execute(
            "INSERT INTO account_credentials VALUES(NULL, ?, ?)", (
                username,
                password
            )
        )
        self.conn.commit()

    def delete(self):
        self.cur.execute(
            "DELETE FROM account_credentials"
        )
        self.conn.commit()

    def __del__(self):
        self.conn.close()
