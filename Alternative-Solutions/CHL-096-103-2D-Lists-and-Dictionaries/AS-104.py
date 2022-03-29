'''
AS-104
After gathering the four names, ages and shoe sizes, ask the
user to enter the name of the person they want to remove from
the list. Delete this row from the data and display the other rows
on separate lines.
'''
#####
# Python By Example
# Exercise 104
# Christopher Hagan
#####

import sys

shoeDictionary = {}
for i in range(0, 4):
    name = input('Enter the name of a person: ')
    age = int(input('Enter {}\'s age: '.format(name)))
    shoeSize = input('And shoe size: ')
    shoeDictionary[name] = {'age': age, 'shoeSize': shoeSize}

personToDelete = input('Which user should be removed from the list: ')

try:
    del shoeDictionary[personToDelete]
except:
    sys.exit('This person does not exist!')

for person in shoeDictionary:
    print('{} is {} years of age and has size {} shoes.'.format(person, shoeDictionary[person]['age'], shoeDictionary[person]['shoeSize']))
    



















