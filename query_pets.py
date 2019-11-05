import sqlite3 as sql
import sys

dbHandle = sql.connect('file:pets.db', uri=True)
cursor = dbHandle.cursor()

id = 0
while id != -1:
    id = input('Enter ID number ')
    if id == '-1':
        sys.exit('Goodbye')
    cursor.execute('SELECT first_name, last_name, age FROM person WHERE id = ?', (id,))
    data = cursor.fetchall()
    if (len(data) < 1):
        print('Error: No person by that ID')
    else:
        print(f'{data[0][0]} {data[0][1]}, {data[0][2]} years old owns')
        cursor.execute('SELECT name, breed, age FROM pet INNER JOIN person_pet on pet.id = person_pet.pet_id WHERE person_pet.person_id = ?', (id,))
        data = cursor.fetchall()
        print(f'{data[0][0]}, a {data[0][1]}, that is {data[0][2]} years old')
