#!/usr/bin/env python3
########################################
### Assignment 6 - Putting it All Together
### Author: Jeremiah Purba
########################################

#imports at top of file
import sqlite3
import os.path
import logging

def debug_config():
    logging.basicConfig(
        level=logging.ERROR,
        format = "[Degrees]:%(asctime)s:%(levelname)s:%(message)s"
    ) #DEBUG,INFO,ERROR,WARNING,CRITICAL

def db_connect(dbfile):
    con = sqlite3.connect(dbfile)
    logging.debug("DB Connected".format())
    return con

def db_cursor(con):
    cur = con.cursor()
    logging.debug("Cursor set".format())
    return cur

def db_runquery(cur,query):
    cur.execute(query)
    result = cur.fetchall()
    logging.debug("DB Query executed and returned".format())
    return result

# To view data in database
def view_db():
    dbfile = 'roster.db'
    try:
        con = db_connect(dbfile)
        cur = db_cursor(con)
        query = 'SELECT * from students'
        rows = db_runquery(cur,query)
        logging.debug("[Info] view_db run query success".format())
    except sqlite3.Error as error:
        logging.error("Error view_db executing query", error)
    finally:
        if con:
            con.close()
            logging.debug("[Info] view_db DB Closed".format())

    print('view_db done - check completed')
    logging.info("view_db Completed.")
    return rows

# To add data into database
def add_db(nm, addr, city, id):
    dbfile = 'roster.db'
    try:
        con = db_connect(dbfile)
        cur = db_cursor(con)
        cur.execute('INSERT INTO students (name, addr, city, id) VALUES (?, ?, ?, ?)',(nm,addr,city,id))
        con.commit()
        logging.debug("[Info] add_db run query success".format())
    except sqlite3.Error as error:
        logging.error("Error add_db executing query", error)
    finally:
        if con:
            con.close()
            logging.debug("[Info] add_db DB Closed".format())

    print('add_db done - check completed')
    logging.info("add_db Completed.")

# To search data in database
def search_db(nm, addr, city):
    dbfile = 'roster.db'
    try:
        con = db_connect(dbfile)
        cur = db_cursor(con)
        cur.execute('SELECT * FROM students WHERE name = ? AND addr = ? AND city = ? ',(nm,addr,city))
        row = cur.fetchall()
        logging.debug("[Info] search_db run query success".format())
    except sqlite3.Error as error:
        logging.error("Error search_db executing query", error)
    finally:
        if con:
            con.close()
            logging.debug("[Info] search_db DB Closed".format())

    print('serch_db done - check completed')
    logging.info("search_db Completed.")
    return row

# To delete data in database
def delete_db(nm):
    dbfile = 'roster.db'
    try:
        con = db_connect(dbfile)
        cur = db_cursor(con)
        cur.execute('DELETE FROM students WHERE name = ? ',(nm,))
        con.commit()
        logging.debug("[Info] delete_db run query success".format())
    except sqlite3.Error as error:
        logging.error("Error delete_db executing query", error)
        return 'Fail'
    finally:
        if con:
            con.close()
            logging.debug("[Info] delete_db DB Closed".format())

    print('delete_db done - check completed')
    logging.info("delete_db Completed.")
    if(cur.rowcount == 0):
        return "No data found"
    else:
        return 'Success'