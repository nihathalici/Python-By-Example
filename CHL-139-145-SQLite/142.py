"""
142
Using the BookInfo database from program 141, display the list of
authors and their place of birth. Ask the user to enter a place of birth and
then show the title, date published and author’s name for all the books
by authors who were born in the location they selected.
"""
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)

print()
location = input("Enter a place of birth: ")
print()

cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author 
FROM Books, Authors WHERE Authors.Name=Books.Author AND Authors.PlaceofBirth=?""",[location])
for x in cursor.fetchall():
    print(x)

db.close()








