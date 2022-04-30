"""
AS-144
Using the BookInfo database, ask the user for an author’s name and then save all the
books by that author to a text file, with each field separated by dashes so it looks as
follows:

1 - De Profundis - Oscar Wilde - 1905
9 - The picture of Dorian Gray - Oscar Wilde - 1890

Open the text file to make sure it has worked correctly.
"""
#####
# Python By Example
# Exercise 144
# Christopher Hagan
#####

import sqlite3

with sqlite3.connect("AS-BookInfo.db") as db:
    cursor = db.cursor()

authorName = input("Enter the name of the author you would like to search for: ")

cursor.execute("SELECT * FROM Books WHERE Author='{}'".format(authorName))
file = open("ASS-BookInfoQuery.txt", "w")
for book in cursor.fetchall():
    file.write('{} - {} - {} - {}\n'.format(book[0], book[1], book[2], book[3]))

file.close()
db.close()
