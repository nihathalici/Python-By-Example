"""
141
Create a new SQL database called BookInfo that will
store a list of authors and the books they wrote.
It will have two tables. The first one should be called
Authors and contain the following data:

The second should be called Books and contain the
following data:
"""

import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Authors(
Name text PRIMARY KEY,
PlaceofBirth text);""")

cursor.execute(""" INSERT INTO Authors(Name, PlaceOfBirth)
VALUES("Agatha Christie", "Torquay")""")
db.commit()

cursor.execute(""" INSERT INTO Authors(Name, PlaceOfBirth)
VALUES("Cecelia Ahern", "Dublin")""")
db.commit()

cursor.execute(""" INSERT INTO Authors(Name, PlaceOfBirth)
VALUES("J.K. Rowling", "Bristol")""")
db.commit()

cursor.execute(""" INSERT INTO Authors(Name, PlaceOfBirth)
VALUES("Oscar Wilde", "Dublin")""")
db.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
ID integer PRIMARY KEY,
Title text,
Author text,
DatePublished integer);""")

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("1", "De Profundis", "Oscar Wilde", "1905")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("2", "Harry Potter and the chamber of secrets", "J.K. Rowling", "1998")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("3", "Harry Potter and the prisoner of Azkaban", "J.K. Rowling", "1999")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("4", "Lyrebird", "Cecelia Ahern", "2017")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("5", "Murder on the Orient Express", "Agatha Christie", "1934")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("6", "Perfect", "Cecelia Ahern", "2017")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("7", "The marble collector", "Cecelia Ahern", "2016")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("8", "The murder on the links", "Agatha Christie", "1923")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("9", "The picture of Dorian Gray", "Oscar Wilde", "1890")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("10", "The secret adversary", "Agatha Christie", "1921")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("11", "The seven dials mystery", "Agatha Christie", "1929")""")
db.commit()

cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished)
VALUES("12", "The year I met you", "Cecelia Ahern", "2014")""")
db.commit()
