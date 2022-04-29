"""
AS-143
Using the BookInfo database, ask the user to enter a year and display all the books
published after that year, sorted by the year they were published.
"""
#####
# Python By Example
# Exercise 143
# Christopher Hagan
#####

import sqlite3

with sqlite3.connect("AS-BookInfo.db") as db:
    cursor = db.cursor()

publicationAfterYear = int(input('Enter the year after which you would like to view published books: '))

print(publicationAfterYear)

cursor.execute("SELECT * FROM Books WHERE DatePublished > {} ORDER BY DatePublished".format(publicationAfterYear))
for book in cursor.fetchall():
    print(book)