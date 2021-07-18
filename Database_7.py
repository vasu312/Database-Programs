# 7) DB_Program - DELETE

import sqlite3

connection = sqlite3.connect("C:/Users/vasud/Desktop/Workstation/Py_Program/Database/MyDatabase_1.db")

cursor = connection.cursor()

cursor.execute("DELETE FROM Students WHERE ID = '4' ")

connection.commit()

print("Succecfully Deleted")

connection.close()