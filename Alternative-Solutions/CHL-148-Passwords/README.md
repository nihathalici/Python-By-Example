Passwords
========================================================

You need to create a program that will store the user ID and passwords for the users of a system.


Passwords-AS-148.py
========================================================
```Python3
import csv, os, shutil

fileName = 'userPw.csv'
columnHeaders = ['User', 'Pword']

def menuTitle(menuName):
    pass

def statusMessage(message):
    pass

def newPwRating():
    rating = 0
    atLeastOneCapital = atLeastOneLower = atLeastOneNumber = atLeastOneSpecial = False
    while (rating < 3):
        newPw = input('Enter the new pword for this user: ')

        if len(newPw) >= 8:
            rating += 1

        for char in newPw:
            if not (atLeastOneCapital) and (char.isupper()):
                rating += 1
                atLeastOneCapital = True
            if not (atLeastOneLower) and (char.islower()):
                rating += 1
                atLeastOneLower = True
            if not (atLeastOneNumber) and (char in '0123456789'):
                rating += 1
                atLeastOneNumber = True
            if not(atLeastOneSpecial) and (char in '!£$%&'):
                rating += 1
                atLeastOneSpecial = True

        if (rating == 5):
            print('\nThis is a strong password.')
        elif (rating >= 3 and rating <= 4):
            print('\nThis password could be improved.')
        else:
            print('\nThis password is too weak, please try again...\n')
            rating = 0

    return newPw

            

def addUser():
    menuTitle('Add A New User')
    newUser = input('Enter the ID of the user: ')
    newPw = newPwRating()
    fileAlreadyExists = os.path.isfile(fileName)
    with open(fileName, "a") as csvFile:
        fileWriter = csv.DictWriter(csvFile, fieldnames= columnHeaders)
        if not fileAlreadyExists:
            fileWriter.writeheader()
        fileWriter.writerow({ 'User' : '{}'.format(newUser), 'Pword': '{}'.format(newPw) })

    statusMessage("User Added")

def createListOfUsers():
    pass

def changePword():
    pass

def displayUsers():
    pass

userSelection = '0'
while (userSelection != '4'):
    print("""\n===========\nPwords\n===========
1) Create a new user ID
2) Change a pword
3) Display all User IDs
4) Quit\n""")
    userSelection = input("Enter selection: ")
    if userSelection in ['1', '2', '3', '4']:
        if userSelection == '1':
            addUser()
        elif userSelection == '2':
            changePword()
        elif userSelection == '3':
            displayUsers()
    else:
        print('\n***\nInvalid selection\n***\n')


```

Sample Output
========================================================

![Sample output Passwords](https://github.com/nihathalici/Python-By-Example/blob/main/Alternative-Solutions/CHL-148-Passwords/Pwords_AS-148_sample_output.png)
