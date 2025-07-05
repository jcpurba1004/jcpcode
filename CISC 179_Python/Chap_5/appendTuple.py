"""
File name: appendTuple.py
Purpose: to append an integer to a tuple of integer
Author: Jeremiah Purba
class : CISC 179 Python Programming
"""

intTuple = ('65','123', '1009', '7', '97')
print("Original tuple:", intTuple)

#convert tuple to list so it can be appended
intList = list(intTuple)
intList.append('783')

#convert back from list to tuple
intTuple = tuple(intList)
print("Tuple after append:", intTuple)
