'''
Ask the user to enter their first name. If the length of their first name is
under five characters, ask them to enter their surname and join them together
(without a space) and display the name in upper case. If the length of the
first name is five or more characters, display their first name in lower case.
'''

fname = input('Enter your first name: ')

if len(fname) < 5:
    sname = input('Enter your surname: ').lower()
    print(fname.upper()+sname.upper())
else:
    print(fname.lower())

'''
Author's solution:

name = input("Enter your first name: ")
if len(name) < 5:
    surname = input("Enter your surname: ")
    name = name+surname
    print(name.upper())
else:
    print(name.lower())

'''
