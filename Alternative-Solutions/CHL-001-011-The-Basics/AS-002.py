'''
Ask for the user’s first name and then ask for their surname and display
the output message

Hello [First Name] [Surname].
'''

#####
# Python By Example
# Exercise 002
# Christopher Hagan
#####

firstName = input('What is your forename? ')

secondName = input('And what is your surname? ')

print('Hello {} {}'.format(firstName, secondName))
