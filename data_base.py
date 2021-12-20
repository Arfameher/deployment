import pandas as pd
import sqlite3
import csv

df = pd.read_csv('/home/arfa/deployment/steam.csv')
df.head(1)

conn = sqlite3.connect("database.db") #if the db does not exist, this creates a database.db file in the current directory

c = conn.cursor()
c.execute("DROP TABLE Steam_game1")
#store your table in the database:

c.execute('''CREATE TABLE Steam_game1 
           (steam_appid TEXT PRIMARY KEY,
           name TEXT NOT NULL UNIQUE,
            required_age INTEGER NOT NULL,
            detailed_description TEXT NOT NULL,
            genres TEXT NOT NULL,
            release_date TEXT NOT NULL,
            review_score INTEGER NOT NULL,
            total_positive TEXT NOT NULL,
            total_negative TEXT NOT NULL)
            ''')

filename = '/home/arfa/deployment/steam.csv'
stats = csv.reader(open(filename))

c.executemany("INSERT INTO Steam_game1(steam_appid, name, required_age, detailed_description, genres,release_date, review_score, total_positive, total_negative) VALUES (?,?,?,?,?,?,?,?,?)",
              ((df[3],df[2],df[4],df[6],df[23],df[26],df[31],df[33],df[34]) for df in stats))

for row in c.execute("SELECT * FROM Steam_game1 WHERE steam_appid IS 1198490"):
    print(row)

conn.commit()
conn.close()