"""
144
Using the BookInfo database, ask the user for an author’s name and then save all the
books by that author to a text file, with each field separated by dashes so it looks as
follows:

1 - De Profundis - Oscar Wilde - 1905
9 - The picture of Dorian Gray - Oscar Wilde - 1890

Open the text file to make sure it has worked correctly.
"""
import sqlite3

file = open("BooksList.txt", "w")

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT Name FROM Authors")
for x in cursor.fetchall():
    print(x)

print()
selectauthor = input("Enter an author's name: ")
print()

cursor.execute("SELECT * FROM Books WHERE Author=?", [selectauthor])
for x in cursor.fetchall():
    newrecord = "{} - {} - {} - {}\n".format(str(x[0]), x[1], x[2], str(x[3]))
    file.write(newrecord)

file.close()

db.close()