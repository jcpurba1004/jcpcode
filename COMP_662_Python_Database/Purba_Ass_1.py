#!/usr/bin/env python3
### Assignment 1 - Intro to Databases
### Author: Jeremiah Purba

#imports at top of file
import sqlite3
import os.path


#print program title
def display_title():
    print("Artist List")
    print()

# display the artist list from chinook.db
def display_artist():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "chinook.db")
    #with sqlite3.connect(db_path) as db:

    con = sqlite3.connect(db_path)


    #con = sqlite3.connect('chinook.db')
    # query to select all the elements from the movie table
    query = '''SELECT * FROM artists'''
    cur = con.cursor()
    # run the query
    cur.execute(query)
    # save the results in artists
    artists = cur.fetchall()
    # loop through and print all the artists
    for artist in artists:
        print(artist[1])
    if con:
        con.close()

def main():
    #display the program title
    display_title()
    # display the artist list from chinook.db
    display_artist()
    print("Done - See you next time!")

if __name__ == "__main__":
    main()