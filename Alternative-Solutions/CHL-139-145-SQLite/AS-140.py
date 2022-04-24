"""
AS-140

Using the PhoneBook database from program 139, write a program that will
display the following menu.

  Main Menu

  1) View phone book
  2) Add to phone book
  3) Search for surname
  4) Delete person from phone book
  5) Quit

  Enter your selection:

If the user selects 1, they should be able to view the entire phonebook.
If they select 2, it should allow them to add a new person to the
phonebook. If they select 3, it should ask them for a surname and then
display only the records of people with the same surname.
If they select 4, it should ask for an ID and then delete that record from
the table.
If they select 5, it should end the program.
Finally, it should display a suitable message if they enter an incorrect
selection from the menu.
They should return to the menu after each action, until they select 5.
"""

#####
# Python By Example
# Exercise 140
# Christopher Hagan
#####

import sqlite3

def viewPhoneBook():
    cursor.execute("SELECT * FROM names")
    print('\n***\nView Phone Book\n***\n')
    for entry in cursor.fetchall():
        print(entry)

def addToPhoneBook():
    print('\n***\nAdd entry to Phone Book\n***\n')
    forename = input('Enter the person\'s forename: ')
    surname = input('Enter the person\'s surname: ')
    phoneNumber = input('Enter the person\'s phone number : ')
    if (phoneNumber[5] != ' '):
        phoneNumber = "{} {}".format(phoneNumber[0:5], phoneNumber[5:])
    
    # Use the next available id value to add the user
    cursor.execute("SELECT COUNT(*) FROM names")
    idCount = int(cursor.fetchone()[0]) + 1
    newUserId = 0
    for nextId in range(1, idCount):
        cursor.execute("SELECT * FROM names WHERE id={}".format(nextId))
        if cursor.fetchone() is None:
            newUserId = nextId
            break
    if (newUserId == 0):
        newUserId = idCount
    
    cursor.execute("""INSERT INTO names(id, firstName, secondName, phoneNumber)
        VALUES({} {} {} {})""".format(newUserId, forename, surname, phoneNumber))
    db.commit()


def searchForSurname():
    print('\n***\nSearch for Phone Book entry by Surname\n***\n')
    searchableSurname = input('Enter the Surname to search for: ')

    cursor.execute("SELECT * FROM names WHERE secondName='{}'".format(searchableSurname))
    for entry in cursor.fetchall():
        print(entry)


def deleteFromPhoneBook():
    print('\n***\nDelete entry from Phone Book by ID\n***\n')
    viewPhoneBook()
    idToDelete = input('Enter the ID of the user to delete: ')

    cursor.execute("DELETE FROM names WHERE id={}".format(int(idToDelete)))
    db.commit()

with sqlite3.connect("AS_phonebook.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS names(
id INTEGER PRIMARY KEY,
firstName text NOT NULL,
secondName text NOT NULL,
phoneNumber text NOT NULL);""")

userSelection = '0' 

while (userSelection != '5'):
    userSelection = input("""\n\nMain Menu
\n1) View Phone Book
2) Add to Phone Book
3) Search for Surname
4 Delete person from Phone Book
5) Quit
\nEnter your selection: """)
    
    if userSelection in ['1', '2', '3', '4', '5']:
        if (userSelection == '1'):
            viewPhoneBook()
        elif (userSelection == '2'):
            addToPhoneBook()
        elif (userSelection == '3'):
            searchForSurname()
        elif (userSelection == '4'):
            deleteFromPhoneBook()
    else:
        print('\n***\nInvalid Selection\n***')

db.close() 
print('\n*****\nQuitting program...\n*****')
