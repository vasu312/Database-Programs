# Database-Programs
<h3>Python SQLite Programs using SQLite3</h3>

>>> Python SQLite Database Connection
  
      This section lets you know how to connect to SQLite database in Python using the sqlite3 module.
      Use the following steps to connect to SQLite
      How to Connect to SQLite Database in Python

=> 1.Import sqlite3 module
     
     import sqlite3 statement imports the sqlite3 module in the program. Using the classes 
     and methods defined in the sqlite3 module we can communicate with the SQLite database.
      
=> 2.Use the connect() method
     
      Use the connect() method of the connector class with the database name. To establish a 
      connection to SQLite , you need to pass the database name you want to connect . If you
      specify the database file name that already presents on the disk  , it will connect to 
      it . But if your specified SQLite database file doesn’t  exist , SQLite  creates a new 
      database for you.This method returns the SQLite Connection Object if the connection is 
      successful.
      
=> 3.Use the execute() method

      The execute() methods run the SQL query and return the result.

=> 4.Extract result using fetchall()

      Use cursor.fetchall() or fetchone() or fetchmany() to read query result.

=> 5.Close cursor and connection objects

      use  cursor.clsoe()  and  connection.clsoe() method  to  close  the cursor  and SQLite
      connections after your work completes
