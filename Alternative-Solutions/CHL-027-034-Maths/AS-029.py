'''
Ask the user to enter an integer that is over 500. Work out the
square root of that number and display it to two decimal places.
'''

#####
# Python By Example
# Exercise 029
# Christopher Hagan
#####

import math

num = int(input('Please enter a whole number greater than 500: '))
print('The square root of {} to 2 d.p. is {}'.format(num, round(math.sqrt(num),2)))


