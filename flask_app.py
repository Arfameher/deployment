from flask import Flask, render_template
from flask_navigation import Navigation
import sqlite3
import os
import json
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
  
app = Flask(__name__)
nav = Navigation(app)

# initializing Navigations
nav.Bar('top', [
    nav.Item('Home', 'table'),
    nav.Item('Insights', 'image'),
    nav.Item('Interactive', 'chart')
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
  
    
@app.route('/chart')
def chart():

    # Graph One
    df = pd.read_csv("Dataset/clean_data.csv")
    
    labels = df['platforms'].unique()
    values = df['platforms'].value_counts()

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    graph1JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index1.html', title="home", graph1JSON=graph1JSON)

if __name__ == '__main__':
    port = os.environ.get("PORT")
    app.run(debug=True,host = '0.0.0.0',port=port)