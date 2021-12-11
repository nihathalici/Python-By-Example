'''
Ask the user to enter their first name and then ask them to enter their surname.
Join them together with a space between and display the name and the length
of whole name.
'''

fname = input('Enter your first name: ')
sname = input('Enter your surname: ')
fullname = fname + ' ' + sname
print('Your name is {} characters length.'.format(len(fullname)))

'''
Author's solution:

firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
name = firstname + " " + surname
length = len(name)
print(name)
print(length)
'''
