import sqlite3
from flask import Flask, _app_ctx_stack

app = Flask(__name__)
DATABASE = './location.db'

@app.route('/')
def sql_database():
    db = connect()
    if not db:
        return "Failed to connect"
    else:
        return select_all(db)

def connect():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except Error as e:
        print(e)

    return conn

def select_all(conn):
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute("SELECT * FROM location_values")
    rows = cur.fetchall()

    return str(rows)

# site dict_factory, got it from the sqlite3 docs
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

if __name__ == '__main__':
    app.run()