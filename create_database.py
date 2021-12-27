import pandas as pd
import sqlite3
import csv

df = pd.read_csv('/home/arfa/deployment/Dataset/clean_data.csv')
df.head(1)

conn = sqlite3.connect("database.db") #if the db does not exist, this creates a database.db file in the current directory

c = conn.cursor()
c.execute("DROP TABLE IF EXISTS Steam_game1")
#store your table in the database:

c.execute('''CREATE TABLE Steam_game1 
           (steam_appid TEXT PRIMARY KEY,
           name TEXT NOT NULL UNIQUE,
            required_age INTEGER NOT NULL,
            platforms TEXT NOT NULL,
            genres TEXT NOT NULL,
            release_date TEXT NOT NULL,
            price FLOAT NOT NULL,
            total_reviews INTEGER NOT NULL,
            developer TEXT NOT NULL,
            publisher TEXT NOT NULL,
            review_score INTEGER NOT NULL,
            total_positive TEXT NOT NULL,
            total_negative TEXT NOT NULL)
            ''')

filename = '/home/arfa/deployment/Dataset/clean_data.csv'
stats = csv.reader(open(filename))

c.executemany("INSERT or REPLACE INTO Steam_game1(steam_appid, name, required_age,platforms, genres,\
    release_date,price, total_reviews, developer, publisher,review_score, total_positive,\
         total_negative) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",((df[2],df[1],df[3],df[4],df[6],df[7],df[16],df[13],df[17],df[18],df[9],df[11],df[12]) for df in stats))

for row in c.execute("SELECT * FROM Steam_game1 WHERE steam_appid IS 1198490"):
    print(row)

conn.commit()
conn.close()