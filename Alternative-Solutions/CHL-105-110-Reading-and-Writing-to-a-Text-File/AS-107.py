'''
AS-107
Open the Names.txt file and display the data in Python.
'''

#####
# Python By Example
# Exercise 107
# Christopher Hagan
#####

fileName = 'AS_Names.txt'
file = open(fileName, 'r')

print('The contents of the file "{}" can be seen below :\n\n{}'.format(fileName, file.read()))
