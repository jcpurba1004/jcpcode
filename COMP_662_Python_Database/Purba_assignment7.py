#!/usr/bin/env python3
########################################
### Assignment 7 - Database Analysis
### Author: Jeremiah Purba
########################################

import pandas as pd
import sqlite3
import logging
import matplotlib.pyplot as plt

def db_connect(dbfile):
    con = sqlite3.connect(dbfile)
    logging.debug("DB Connected".format())
    return con

def print_full(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')

def main():
    dbfile = "beers.db"
    con = db_connect(dbfile)

    # Read sqlite query results into a pandas DataFrame
    df = pd.read_sql_query("SELECT * from reviews", con)

    print('#Question 1: How many rows are in the table?')
    print( str(len(df)) )

    print('#Question 2: Describe the table')
    print_full(df.describe())

    print('#Question 3: How many entries are there for each brewery')
    print(df.groupby(['brewery_name']).size())

    print('#Question 4: Find all entries are low alcohol.  Alcohol by volume (ABV) less than 1%')
    low_abv = df[df.beer_abv < 1]
    print_full(low_abv)

    print('#Question 5:How many reviews are there for low ABV beers?')
    print(len(low_abv))
    # print('There are ' + str(len(low_abv)) + ' reviews for low ABV beers')

    print('#Question 6:Group  the AVB beers by beer and count')
    grouping = low_abv.groupby('beer_name')
    print(grouping.size())

    print("""#Question 7:How consistent are the O Douls overall scores?""")
    odouls = low_abv[low_abv.beer_name == "O'Doul's"]['review_overall']
    print(odouls)

    print("""#Question 8:Plot a histogram of O'Douls overall scores (may need to close window to continue)""")
    odouls.hist()
    plt.show()

    print("""#Question 9:For O'Douls, what are the mean and standard deviation for the O'Doul's overall scores?""")
    print(odouls.mean())
    print(odouls.std())

    print("""#Question 10:Draw a boxplot of the low_abv data (may need to close window to continue)""")
    low_abv.boxplot(figsize=(12,10))
    plt.show()

if __name__ == '__main__':
    main()