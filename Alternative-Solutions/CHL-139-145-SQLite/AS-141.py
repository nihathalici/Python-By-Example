"""
AS-141
Create a new SQL database called BookInfo that will
store a list of authors and the books they wrote.
It will have two tables. The first one should be called
Authors and contain the following data:

The second should be called Books and contain the
following data:
"""

#####
# Python By Example
# Exercise 141
# Christopher Hagan
#####

import sqlite3

authorsToAdd = ({'Name' : 'Agatha Christie', 'Place of Birth' : 'Torquay'},
                {'Name' : 'Cecelia Ahern', 'Place of Birth' : 'Dublin'},
                {'Name' : 'J.K. Rowling', 'Place of Birth' : 'Bristol'},
                {'Name' : 'Oscar Wilde', 'Place of Birth' : 'Dublin'})

booksToAdd = ({'ID' : 1, 'Title' : 'De Profundis', 'Author' : 'Oscar Wilde', 'Date Published' : 1905},
              {'ID' : 2, 'Title' : 'Harry Potter and the Chamber of Secrets', 'Author' : 'J.K. Rowling', 'Date Published' : 1998},
              {'ID' : 3, 'Title' : 'Harry Potter and the Prisoner of Azkaban', 'Author' : 'J.K. Rowling', 'Date Published' : 1999},
              {'ID' : 4, 'Title' : 'Lyrebird', 'Author' : 'Cecelia Ahern', 'Date Published' : 2017},
              {'ID' : 5, 'Title' : 'Murder on the Orient Express', 'Author' : 'Agatha Christie', 'Date Published' : 1934},
              {'ID' : 6, 'Title' : 'Perfect', 'Author' : 'Cecelia Ahern', 'Date Published' : 2017},
              {'ID' : 7, 'Title' : 'The Marble Collector', 'Author' : 'Cecelia Ahern', 'Date Published' : 2016},
              {'ID' : 8, 'Title' : 'The Murder on the Links', 'Author' : 'Agatha Christie', 'Date Published' : 1923},
              {'ID' : 9, 'Title' : 'The Picture of Dorian Gray', 'Author' : 'Oscar Wilde', 'Date Published' : 1890},
              {'ID' : 10, 'Title' : 'The Secret Advesary', 'Author' : 'Agatha Christie', 'Date Published' : 1921},
              {'ID' : 11, 'Title' : 'The Seven Dials Mystery', 'Author' : 'Agatha Christie', 'Date Published' : 1929},
              {'ID' : 12, 'Title' : 'The Year I Met You', 'Author' : 'Cecelia Ahern', 'Date Published' : 2014})
              
with sqlite3.connect("AS-BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
    Name text PRIMARY KEY,
    'Place of Birth' text NOT NULL
);""")

for author in authorsToAdd:
    cursor.execute("""INSERT INTO Authors(Name, 'Place of Birth')
        VALUES(\"{}\", \"{}\");""".format(author['Name'], author['Place of Birth']))
    db.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
ID INTEGER PRIMARY KEY,
Title text NOT NULL,
Author text NOT NULL,
'Date Published' INTEGER NOT NULL);""")

for book in booksToAdd:
    cursor.execute("""INSERT INTO Books(ID, Title, Author, 'Date Published')
        VALUES({}, '{}', '{}', {});""".format(book['ID'], book['Title'], book['Author'], book['Date Published']))
    db.commit()

db.close()