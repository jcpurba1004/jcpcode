import pandas as pd
import sqlite3
import os
import logging
import matplotlib.pyplot as plt
# import numpy as np

dbfile = 'degrees2.db'
#connect to sqlite database
def db_connect(dbfile):
    con = sqlite3.connect(dbfile)
    logging.debug("DB Connected".format())
    return con

def main():
    # dbfile = 'C:\data\Jeremiah\programming\github\codes\python\COMP_662\degrees2.db'
    dbfile = 'degrees2.db'
    programname = "Visualizing Data"

    #connect to sqlite database
    con = db_connect(dbfile)

    # Read sqlite query results into a pandas DataFrame
    df = pd.read_sql_query("SELECT * from degrees", con)

    #gca means "get current axes", putting all the graphs on the same plot.
    ax = plt.gca()

    #select 4 columns to plot
    for degree in df.columns[6:10]:
        df.plot(x="Year", y=degree, kind='line', ax=ax)

    plt.show()

if __name__ == '__main__':
    main()