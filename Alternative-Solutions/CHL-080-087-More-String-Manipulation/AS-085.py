'''
AS-085
Ask the user to type in their name and then tell
them how many vowels are in their name.
'''
#####
# Python By Example
# Exercise 085
# Christopher Hagan
#####

name = input('Please enter your name: ')
vowels = 0
for letter in name:
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowels += 1

print('{}, your name contains {} vowels.'.format(name, vowels))
