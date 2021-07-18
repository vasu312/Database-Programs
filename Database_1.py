# 1) DB_Program - Fetch All

import sqlite3

connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Students")

data = cursor.fetchall()

for value in data:
    print (value)

