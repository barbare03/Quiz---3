import requests
import json
import sqlite3

#1
r= requests.get("https://ghibliapi.herokuapp.com/films")
r = requests.get('https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all')
print(r)
print(r.status_code)
print(r.headers)
print(r.text)

#2
res = r.json()
with open('Ghibli.json', 'w') as f:
    json.dump(res, f, indent=4)

#3

print('Name of the anime:',res[2]["title"],'\nRelease Date:',res[2]["release_date"])
print('Name of the anime:',res[7]["title"],'\nDirector:',res[7]["director"])
print('Name of the anime:',res[15]["title"],'\nRunning Time:',res[15]["running_time"])

#4
"""ცხრილში მოცემულია ინფორმაცია ანიმეების დასახელების,რეჟისორის და გამოშვების წლის შესახებ"""
conn = sqlite3.connect('Ghibli_movies.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS ghibli 
             (id INTEGER PRIMARY KEY AUTOINCREMENT ,
             title VARCHAR(50),
             director VARCHAR(50),
             release_date INTEGER
             )''')

all_rows = []
for each in res:
    title = each["title"]
    director = each["director"]
    releaseDate = each["release_date"]
    row = (title, director, releaseDate)
    all_rows.append(row)


c.executemany('INSERT INTO ghibli(title, director, release_date) VALUES (?, ?, ?)',all_rows)
conn.commit()
conn.close()