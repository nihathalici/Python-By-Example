"""
AS-146
Shift Code:
A shift code is where a message can be easily encoded and is one of the simplest codes to
use. Each letter is moved forwards through the alphabet a set number of letters to be
represented by a new letter.
"""

#####
# Python By Example
# Exercise 145
# Christopher Hagan
#####

codeString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '

def displayMenu():
    print("""\nMain Menu\n==========
1) Make a code
2) Decode a message
3) Quit\n""")
    choice = input('Enter your selection: ')
    return choice

def userEntry(operationText):
    pass

def displayMessage(message):
    pass

def encrypText():
    pass

def decryptText():
    pass

userSelection = '0'
while (userSelection != '3'):
    userSelection = displayMenu()
    if userSelection in ['1', '2', '3']:
        if userSelection == '1':
            encrypText()
        elif userSelection == '2':
            decryptText()
    
    else:
        print('\n***\nInvalid selection, please try again...\n***\n')

print('\n\n*****\nQuitting program at user request\n*****\n\n')