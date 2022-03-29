'''
AS-102
Ask the user to enter the name, age and shoe size for four people. Ask for the name
of one of the people in the list and display their age and shoe size.
'''

#####
# Python By Example
# Exercise 102
# Christopher Hagan
#####

import sys

shoeDictionary = {}

for i in range(0, 4):
    name = input('Enter the name of a person: ')
    age = int(input('Enter {}\'s age: '.format(name)))
    shoeSize = input('And shoe size: ')
    shoeDictionary[name] = {'age': age, 'shoeSize: ': shoeSize}

displayName = input('Which user details would you like to view: ')

try:
    print(shoeDictionary[displayName])
except:
    sys.exit('This person does not exist!')
    
























