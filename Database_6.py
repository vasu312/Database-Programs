# 6) DB_Program - WHERE

import sqlite3

connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")

cursor = connection.cursor()

cursor.execute("SELECT ID,Name FROM Students WHERE ID >2")

data = cursor.fetchall()

print(data,sep='\n')