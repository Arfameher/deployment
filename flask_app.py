import sqlite3
from flask import Flask, render_template
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('./database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    games = conn.execute('SELECT * FROM Steam_game1').fetchall()
    conn.close()
    return render_template('index.html', games=games)

@app.route('/game')
def game():
    conn = get_db_connection()
    games = conn.execute("SELECT * FROM Steam_game1").fetchall()
    #return f"<h1>The id is {games[1]['name']}.<br>The name is .<br>The release_date is .<br>"
    return render_template('game.html', games=games)

if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)
    app.run(debug=True,host = '0.0.0.0',port=port)
