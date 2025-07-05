#!/usr/bin/env python3

# Assignment 1 - Read Movie SQLite
# Author: Jeremiah, Purba

#imports at top of file

import sqlite3
#import os.path

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#db_path = os.path.join(BASE_DIR, "movies.sqlite")
#with sqlite3.connect(db_path) as db:

#con = sqlite3.connect(db_path)
con = sqlite3.connect('movies.sqlite')

#con = sqlite3.connect('movies.sqlite')

cur = con.cursor()

#query to select all the elements from the movie table
query = '''SELECT * FROM Movie'''

#run the query
cur.execute(query)

#save the results in movies
movies = cur.fetchall()

#loop through and print all the movies
for movie in movies:
    print(movie[2] , " " ,movie[3] , " " ,  movie[4])

if con:
    con.close()