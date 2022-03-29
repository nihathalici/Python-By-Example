'''
AS-103
Adapt program 102 to display the names and ages of all the people in
the list but do not show their shoe size.
'''

#####
# Python By Example
# Exercise 103
# Christopher Hagan
#####

shoeDictionary = {}

for i in range(0, 4):
    name = input('Enter the name of a person: ')
    age = int(input('Enter {}\'s age: '.format(name)))
    shoeSize = input('And shoe size: ')
    shoeDictionary[name] = {'age': age, 'shoeSize: ': shoeSize}

for person in shoeDictionary:
    print('{} is {} years of age'.format(person, shoeDictionary[person]['age']))
    

