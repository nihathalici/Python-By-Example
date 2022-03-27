'''
AS-095
Create an array of five numbers between 10 and 100 which each have
two decimal places. Ask the user to enter a whole number between 2 and 5.
If they enter something outside of that range, display a suitable error message
and ask them to try again until they enter a valid amount. Divide each of the
numbers in the array by the number the user entered and display the answers
shown to two decimal places.
'''

#####
# Python By Example
# Exercise 095
# Christopher Hagan
#####

from array import *

nums = array('f', [15.26, 47.23, 58.94, 67.81, 96.12])
print(nums)
validNumber = False
while not validNumber:
    divisor = int(input('Enter a whole number between 2 and 5 to divide the '
                        'numbers in the array by: '))
    if (divisor < 2) or (divisor > 5):
        print('Invalid value entered.')
    else:
        validNumber = True

for i in nums:
    print('{} divided by {} is {} (2 d.p.)'.format(i, divisor, round(i / divisor, 2)))























