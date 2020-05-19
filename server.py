import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def get_devotional():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.row_factory = sqlite3.Row

    get_query = '''
    SELECT * FROM devotional;
    '''

    cursor.execute(get_query)
    results = cursor.fetchall()

    rowarray_list = []
    for row in results:
        d = dict(zip(row.keys(), row))
        rowarray_list.append(d)

    conn.close()

    return jsonify(rowarray_list)


if __name__ == '__main__':
    app.run()
