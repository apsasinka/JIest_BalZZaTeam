from flask import Flask, render_template, request, redirect, flash 
import sqlite3 
from server import ServerCon 

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.template_folder = 'templates'

ex_server = ServerCon()


@app.route('/')
def index():
    conn = ex_server.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Stuffs")
    rows = cursor.fetchall()
    conn.close()

    return render_template('index.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
