import sqlite3 as sql
import os
os.chdir('c:/Users/silaz/github/capstone/is211/w10')

dbHandle = sql.connect('file:pets.db', uri=True)
cursor = dbHandle.cursor()
dbs = ['person', 'pet', 'person_pet']
for db in dbs:
    cursor.execute(f'DROP TABLE IF EXISTS {db}')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    );
        ''')
dbHandle.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    );
''')
dbHandle.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS person_pet (
        person_id INTEGER,
        pet_id INTEGER
    );
''')
dbHandle.commit()

cursor.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?)", (1, 'James', 'Smith', 41))
cursor.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?)", (2, 'Diana', 'Greene', 24))
cursor.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?)", (3, 'Sara', 'White', 27))
cursor.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?)", (4, 'William', 'Gibson', 23))
dbHandle.commit()

cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)", (1, 'Rusty', 'Dalmation', 4, 1))
cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)", (2, 'Bella', 'Alaskan Malamute', 3, 0))
cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)", (3, 'Max', 'Cocker Spaniel', 1, 0))
cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)", (4, 'Rocky', 'Beagle', 7, 0))
cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)", (5, 'Rufus', 'Cocker Spaniel', 1, 0))
cursor.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)", (6, 'Spot', 'Bloodhound', 2, 1))
dbHandle.commit()

cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)", (1, 1))
cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)", (1, 2))
cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)", (2, 3))
cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)", (2, 4))
cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)", (3, 5))
cursor.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)", (4, 6))
dbHandle.commit()
