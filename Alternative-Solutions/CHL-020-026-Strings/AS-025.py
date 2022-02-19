'''
AS-025
Ask the user to enter their first name. If the length of their first name is
under five characters, ask them to enter their surname and join them together
(without a space) and display the name in upper case. If the length of the
first name is five or more characters, display their first name in lower case.
'''

#####
# Python By Example
# Exercise 025
# Christopher Hagan
#####

firstName = input('Please enter your first name: ')
if len(firstName) < 5:
    surname = input('And your surname: ')
    fullName = firstName + surname
    print('Your name in upper case is {}'.format(fullName.upper()))
else:
    print('Your name in lower case is {}'.format(firstName.lower()))


