'''
AS-080
Ask the user to enter their first name and then display the length of their
first name. Then ask for their surname and display the length of their surname.
Join their first name and surname together with a space between and display
the result. Finally, display the length of their full name (including the space).
'''

#####
# Python By Example
# Exercise 080
# Christopher Hagan
#####

firstName = input('Enter your first name: ')
print('The length of your first name is {}.'.format(len(firstName)))
surname = input('Enter your surname: ')
print('The length of your surname is {}'.format(len(surname)))
fullName = '{} {}'.format(firstName, surname)
print('That would mean your full name is: {}'.format(fullName))
print('The length of your full name, including the space is {} characters.'.format(len(fullName)))
