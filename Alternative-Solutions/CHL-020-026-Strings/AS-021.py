'''
AS-021
Ask the user to enter their first name and then ask them to enter their surname.
Join them together with a space between and display the name and the length
of whole name.
'''
#####
# Python By Example
# Exercise 021
# Christopher Hagan
#####

firstName = input('What is your first name? ')
surname = input('What is your surname? ')
fullName = firstName + ' ' + surname
print('Your full name is {}, which is {} characters long.'.format(fullName, (len(firstName) + len(surname))))
