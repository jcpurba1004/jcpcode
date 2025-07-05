#!/usr/bin/env python3

# Assignment 1 - Read Name SQLite
# Author: Jeremiah, Purba

#imports at top of file

import sqlite3
#import os.path

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#db_path = os.path.join(BASE_DIR, "names.sqlite")
#with sqlite3.connect(db_path) as db:

#con = sqlite3.connect(db_path)

con = sqlite3.connect('my_database.db')

cur = con.cursor()

#query to select all the elements from the name table
query = '''SELECT * FROM users'''

#run the query
cur.execute(query)

#save the results in names
users = cur.fetchall()

#loop through and print all the names
for user in users:
    print(users[2])

if con:
    con.close()