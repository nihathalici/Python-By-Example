'''
AS-036
Alter program 035 so that it will ask the user to enter their name and
a number and then display their name that number of times.
'''

#####
# Python By Example
# Exercise 036
# Christopher Hagan
#####

name = input('Please enter your name: ')
repetitions = int(input('How many times should I say your name: '))
for i in range(0, repetitions):
    print(name)
