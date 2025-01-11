import os
import sqlite3

if os.path.exists("solution_hw.db"):
    os.remove("solution_hw.db")
else:
    print("The file does not exist")
    
conn = sqlite3.connect('solution_hw.db')  # creates a connector

conn.row_factory = sqlite3.Row  # allow me to use column name

cursor = conn.cursor()  # creates a cursor

cursor.execute('CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER);')
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("INSERT INTO shopping VALUES (1, 'Avokado', 5);")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("INSERT INTO shopping VALUES (2, 'Milk', 2);")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("INSERT INTO shopping VALUES (3, 'Bread', 3);")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("INSERT INTO shopping VALUES (4, 'Chocolate', 8);")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("INSERT INTO shopping VALUES (5, 'Bamba', 5);")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("INSERT INTO shopping VALUES (6, 'Orange', 10);")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("SELECT * FROM shopping")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("SELECT * FROM shopping WHERE amount > 5")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("DELETE from shopping WHERE name like 'Orange';")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))

cursor.execute("SELECT COUNT(*)from shopping")
rows = cursor.fetchall()
for row in rows:
    print(tuple(row))
cursor.execute("SELECT * FROM shopping WHERE id > 0")

rows = cursor.fetchall()
for row in rows:
    print(tuple(row))

conn.close()
