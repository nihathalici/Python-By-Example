'''
AS-084
Ask the user to type in their postcode.
Display the first two letters in uppercase.
'''

#####
# Python By Example
# Exercise 084
# Christopher Hagan
#####

postcode = input('Enter your postcode: ')
print('The first two characters of your postcode are {}.'.format(postcode[0:2].upper()))
