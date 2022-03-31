'''
AS-108
Open the Names.txt file. Ask the user to input a new name.
Add this to the end of the file and display the entire file.
'''
#####
# Python By Example
# Exercise 108
# Christopher Hagan
#####

file = open('AS_Names.txt', 'a')
anotherName = input('Enter another name to add to the file: ')
file.write('{}\n'.format(anotherName))
file.close()

fileContents = open('AS_Names.txt', 'r')
print('The contents of the file are as follows: \n\n{}'.format(fileContents.read()))
