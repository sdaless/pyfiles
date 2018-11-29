#Sara D'Alessandro
#October 31, 2018
#This program prompts the user to enter a list of names and organizes them.

import re

nlist = input("Please enter your list of names, separated by semicolons: ")

person = nlist.split(';')

print("You entered: ")

print(*person, sep = "\n")

print("Thanks for using my name organizer, I guess.")
