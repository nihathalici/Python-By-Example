
Shift Code
========================================================

A shift code is where a message can be easily encoded and is one of the simplest codes to use. Each letter is moved forwards through the alphabet a set number of letters to be represented by a new letter. For instance, “abc” becomes “bcd” when the code is shifted by one (i.e. each letter in the alphabet is moved forward one character).

AS-146.py
========================================================
```Python3
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

def encryptText():
    pass

def decryptText():
    pass


userSelection = '0'
while (userSelection != '3'):
    userSelection = displayMenu()
    if userSelection in ['1', '2', '3']:
        if userSelection == '1':
            encryptText()
        elif userSelection == '2':
            decryptText()

    else:
        print('\n***\nInvalid selection, please try again...\n***\n')

print('\n\n*****\nQuitting program at user request\n*****\n\n')

```

Sample Output
========================================================


![Sample output Shift Code](https://github.com/nihathalici/Python-By-Example/blob/main/Alternative-Solutions/CHL-146-Shift-Code/sample-output-AS-146.png)
