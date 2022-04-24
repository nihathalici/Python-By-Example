"""
AS-139
Create an SQL database called PhoneBook that
contains a table called Names with the following data:
"""
#####
# Python By Example
# Exercise 139
# Christopher Hagan
#####

import sqlite3

entriesToAdd = ({'ID':1, 'firstName':'Simon', 'secondName':'Howells', 'phoneNumber': '01223 349752'},
                {'ID':2, 'firstName':'Karen', 'secondName':'Phillips', 'phoneNumber': '01954 295773'},
                {'ID':3, 'firstName':'Darren', 'secondName':'Smith', 'phoneNumber':'01583 749012'},
                {'ID':4, 'firstName':'Anne', 'secondName':'Jones', 'phoneNumber':'01323 567322'},
                {'ID':5, 'firstName':'Mark', 'secondName':'Smith', 'phoneNumber':'01223 855534'})

with sqlite3.connect("AS_phonebook.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS names(
id INTEGER PRIMARY KEY,
firstName text NOT NULL,
secondName text NOT NULL,
phoneNumber text NOT NULL);""")

for entry in entriesToAdd:
    cursor.execute("""INSERT INTO names(id, firstName, secondName, phoneNumber)
        VALUES({},\"{}\",\"{}\",\"{}\")""".format(entry['ID'], entry['firstName'], entry['secondName'], entry['phoneNumber']))
    db.commit()

db.close()