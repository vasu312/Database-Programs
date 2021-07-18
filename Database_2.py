# 2) DB_Program - Fetch One

import sqlite3

connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Students")

data = cursor.fetchone()

while data is not None: #Data Value
    print(data)
    data = cursor.fetchone() #Next Line

