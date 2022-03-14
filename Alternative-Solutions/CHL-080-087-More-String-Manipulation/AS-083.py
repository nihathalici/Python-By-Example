'''
AS-083
Ask the user to type in a word in upper case. If they type it in lower case,
ask them to try again. Keep repeating this until they type in a message all
in uppercase.
'''

#####
# Python By Example
# Exercise 083
# Christopher Hagan
#####

repeat = True
while repeat:
    word = input('Enter a word in upper case: ')
    if word.isupper():
        repeat = False
    else:
        print('Please try again...')
