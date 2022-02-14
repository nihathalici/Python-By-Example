'''
Ask the user to enter a number over 100 and then enter a number under 10 and tell them
how many times the smaller number goes into the larger number in a user-friendly format.
'''

#####
# Python By Example
# Exercise 011
# Christopher Hagan
#####

numberOverHundred = int(input('Please enter a number over 100: '))

numberUnderTen = int(input('Now enter a number under 10: '))

print('{} goes into {} a total of {} times.'.format(numberUnderTen, numberOverHundred, (numberOverHundred//numberUnderTen)))
