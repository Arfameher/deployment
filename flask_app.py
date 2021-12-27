from flask import Flask, render_template
from flask_navigation import Navigation
import sqlite3
import os
#import plotly
#import plotly.express as px
  
app = Flask(__name__)
nav = Navigation(app)

# initializing Navigations
nav.Bar('top', [
    nav.Item('Home', 'table'),
    nav.Item('Insights', 'image'),
])

def get_db_connection():
    conn = sqlite3.connect('./database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('layout.html', title="Index")

@app.route('/table')
def table():
    conn = get_db_connection()
    games = conn.execute('SELECT * FROM Steam_game1').fetchall()
    conn.close()
    return render_template('table.html', games=games)

@app.route('/image')
def image():
    return render_template('image.html')
  

if __name__ == '__main__':
    port = os.environ.get("PORT")
    app.run(debug=True,host = '0.0.0.0',port=port)