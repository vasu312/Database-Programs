# 5) DB_Program - Count

import sqlite3

connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*)FROM Students")

data = cursor.fetchall()

print(data)
