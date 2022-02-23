'''
AS-039
Ask the user to enter a number between 1 and 12
and then display the times table for that number.
'''

#####
# Python By Example
# Exercise 039
# Christopher Hagan
#####


number = int(input('Which times tables should be shown: '))
for i in range(1, 13):
    print('{} times {} = {}'.format(number, i, (i*number)))
