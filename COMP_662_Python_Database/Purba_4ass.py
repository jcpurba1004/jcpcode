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
    # get current directory
    path = os.getcwd()
    db_path = os.path.join(path, dbfile)
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
    print()

def update_DB(con,cur):
    try:
        cur.execute("UPDATE Movie SET year = ? WHERE name = ?", (1995, 'Toy Story'))
        logging.debug("Update Toy Story Year")
    except sqlite3.IntegrityError:
        logging.debug("UPDATE error")
    # Commit the changes to the database
    con.commit()

def print_query(cur ,name):
    # retrieve_query = ('SELECT * FROM Movie WHERE name = "?" ',(name))
    cur.execute("SELECT * FROM Movie WHERE name = ? ", (name,))
    users = cur.fetchall()
    # loop through and print all the artists
    for user in users:
        print(user[0] , " " ,user[1] , " " ,  user[2], " " ,  user[3], " " ,  user[4])
    # retrieve_val = "Toy Story"
    # run the query
    # cur.execute(retrieve_query)
    # save the results in artists
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
    #programname = "Welcome to the MovieDB!"
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "dbmovies.sqlite")
    #with sqlite3.connect(db_path) as db:

    con = sqlite3.connect(db_path)
    debug_config()
    display_title()
    db_checkfile(dbfile)
    #con = db_connect(dbfile)
    cur = db_cursor(con)
    toy = "Toy Story"
    print_query(cur, toy)
    update_DB(con, cur)
    print("After update")
    #cur.execute("UPDATE Movie SET year = ? WHERE movieID = ?", (1995, 5))
    print_query(cur,toy)
    print()
    print("Before delete")
    Lawrence = "Lawrence of Arabia"
    print_query(cur, Lawrence)
    delete_DB(con, cur)
    print("After delete")
    print_query(cur, Lawrence)
    #Please enter the year to lookup:
    user_input = ""
    while user_input.lower() != "n":
        search_year = int(input("Please enter the year to lookup: "))
        search_query = "SELECT * FROM Movie WHERE year LIKE ?"
        #search_year = "SELECT * FROM Movie WHERE year = .movie_year"
        cur.execute(search_query, (f"%{search_year}%",))
        #cur.execute(search_query, _parameters {"movie_year",movie_year})
        users = cur.fetchall()
        # loop through and print all the artists
        if users:
            for user in users:
                print(user[0] , " " ,user[1] , " " ,  user[2], " " ,  user[3], " " ,  user[4])
        else:
            print("Sorry, no movie in our database for ",search_year)
        print()
        user_input = input("Look up another year (y/n)? ")

    if con:
        con.close()
        logging.debug("DB Closed")

    print('Bye for now - see you at the movies!')

if __name__ == "__main__":
    main()

    """
        try:
            cur.execute("UPDATE Movie SET year = ? WHERE name = ?", (1995, 'Toy Story'))
            logging.debug("Update Toy Story Year")
        except sqlite3.IntegrityError:
            logging.debug("UPDATE error")

        # Commit the changes to the database
        con.commit()
    """

    """
        retrieve_query = '''SELECT * FROM Movie WHERE name = 'Toy Story' '''
        # retrieve_val = "Toy Story"
        # run the query
        cur.execute(retrieve_query)
        # save the results in artists
        users = cur.fetchall()
        # loop through and print all the artists
        for user in users:
            print(user[0] , " " ,user[1] , " " ,  user[2], " " ,  user[3], " " ,  user[4])
       """