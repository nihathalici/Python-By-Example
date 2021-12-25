'''
Using the Books.csv file from program 111, ask the user to enter another
record and add it to the end of the file. Display each row of the .csv file
on a separate line.
'''

import csv

file = open("Books.csv", "a")
rec = "Around the World in Eighty Days, Jules Verne, 1872\n"
file.write(rec)
file.close()

file = open("Books.csv", "r")
for line in file:
    print(line)
file.close()

