"""
AS-142
Using the BookInfo database from program 141, display the list of
authors and their place of birth. Ask the user to enter a place of birth and
then show the title, date published and author’s name for all the books
by authors who were born in the location they selected.
"""
#####
# Python By Example
# Exercise 142
# Christopher Hagan
#####

import sqlite3

with sqlite3.connect("AS-BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""SELECT * FROM Authors;""")
for author in cursor.fetchall():
    print(author)

authorBirthPlace = input('Enter the place of birth of the author(s) you would like to search: ')

cursor.execute("SELECT * FROM Books WHERE Author IN (SELECT Name FROM Authors WHERE PlaceOfBirth='{}');".format(authorBirthPlace))
for x in cursor.fetchall():
    print(x)
