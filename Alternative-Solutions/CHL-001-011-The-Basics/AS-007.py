'''
Ask the user for their name and their age. Add 1 to their age and display the output
[Name] next birthday you will be [new age].
'''

#####
# Python By Example
# Exercise 007
# Christopher Hagan
#####

name = input('What is your name? ')
age = int(input('And what is your age? '))
print('{} next birthday you will be {}'.format(name, age + 1))
