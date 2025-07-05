#!/usr/bin/env python3

# Assignment 1 - Sample Assignment
# Author: Jeremiah, Purba

#imports at top of file
import random

#print program title
def display_title():
    print("Random Number Generator")
    print()

#function to display and return a random number
def display_random(seed):
    rand =random.randint(0,seed)
    print("Winning number: ",rand)
    return rand

def main():
    #display the program title
    display_title()

    #loop until user wants to end the programo
    option = ""
    while option != "n":
        display_random(42)
        option = input("Display another winning number? (y/n)")
        if option.lower()!='y':
            break

    print("Bye!")

if __name__ == "__main__":
    main()