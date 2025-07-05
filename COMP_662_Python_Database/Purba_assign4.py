#!/usr/bin/env python3
### Assignment 4 - More SQL
### Author: Jeremiah Purba

#imports at top of file
import sqlite3
import logging
import os.path

# For logging
def debug_config():
	logging.basicConfig(
        level=logging.DEBUG,
        format = "[Movies]:%(asctime)s:%(levelname)s:%(message)s"
    )  #DEBUG,INFO,ERROR,WARNING,CRITICAL

# For checking file
def db_checkfile(dbfile):
    if os.path.exists(dbfile) and os.path.getsize(dbfile) > 0:
        logging.debug("{} found and not zero size".format(dbfile))
    else:
        logging.error("{a} not found or zero size".format(a=dbfile))

# For connecting to DB
def db_connect(dbfile):
    con = sqlite3.connect(dbfile)
    logging.debug("DB Connected".format())
    return con

# For cursor
def db_cursor(con):
    cur = con.cursor()
    logging.debug("Cursor set".format())
    return cur

#print program title
def display_title():
    print("Welcome to the MovieDB!")

def update_DB(con,cur):
    try:
        cur.execute("UPDATE Movie SET year = ? WHERE name = ?", (1995, 'Toy Story'))
        logging.debug("Update Toy Story Year")
    except sqlite3.IntegrityError:
        logging.debug("UPDATE error")
    # Commit the changes to the database
    con.commit()

def delete_DB(con,cur):
    try:
        cur.execute("DELETE FROM Movie WHERE name = ?", ('Lawrence of Arabia',))
        logging.debug("Delete Lawrence of Arabia")
    except sqlite3.IntegrityError:
        logging.debug("Delete error")
    # Commit the changes to the database
    con.commit()

def main():
    dbfile = "dbmovies.sqlite"
    debug_config()
    display_title()
    db_checkfile(dbfile)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "dbmovies.sqlite")

    con = sqlite3.connect(db_path)
    # con = db_connect(dbfile)
    cur = db_cursor(con)
    update_DB(con, cur)
    delete_DB(con, cur)
    #Please enter the year to lookup:
    user_input = "y"
    while user_input.lower() == "y":
        search_year = int(input("Please enter the year to lookup: "))
        # Join Query
        join_query = ("SELECT Category.*, Movie.* FROM Category INNER JOIN Movie "
                      "ON Category.categoryID = Movie.categoryID "
                      "WHERE Movie.year LIKE ?")
        cur.execute(join_query, (f"%{search_year}%",))
        users = cur.fetchall()
        # loop through and print all the artists
        if users:
            for user in users:
                print(user[4] , " " ,user[5] , " " ,  user[6], " " ,  user[1])
        else:
            print("Sorry, no movie in our database for ",search_year)
        user_input = input("Look up another year (y/n)? ").lower()

    if con:
        con.close()
        logging.debug("DB Closed")

    print('Bye for now - see you at the movies!')

if __name__ == "__main__":
    main()
