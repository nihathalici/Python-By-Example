'''
Ask the user to enter their first name and surname in lower case.
Change the case to title case and join them together. Display the
finished result.
'''

fname = input('Enter your first name: ').lower()
sname = input('Enter your surname: ').lower()
fullname = fname + ' ' + sname
print('Your name is {}.'.format(fullname.title()))

'''
Author's solution:

firstname = input('Enter your first name in lowercase: ')
surname = input('Enter your surname in lowercase: ')
firstname = firstname.title()
surname = surname.title()
name = firstname + " " + surname
print(name)
'''
