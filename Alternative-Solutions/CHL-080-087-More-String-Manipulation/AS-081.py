'''
AS-081
Ask the user to type in their favourite school subject. Display it with
“-” after each letter, e.g. S-p-a-n-i-s-h-.
'''

#####
# Python By Example
# Exercise 081
# Christopher Hagan
#####

favSubject = input('Enter your favourite school subject: ')
for letter in favSubject:
    print(letter, end='-')
print()
