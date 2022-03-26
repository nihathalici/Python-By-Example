'''
AS-094
Display an array of five numbers. Ask the user to select one of the numbers.
Once they have selected a number, display the position of that item in the
array. If they enter something that is not in the array, ask them to try
again until they select a relevant item.
'''

#####
# Python By Example
# Exercise 094
# Christopher Hagan
#####

from array import *

nums = array('i', [7, 18, 47, 58, 94])
validChoice = False

print(nums)

while not validChoice:
    userChoice = int(input('Enter a number to remove: '))
    if userChoice in nums:
        print('{} is in position {} of the array.'.format(userChoice, nums.index(userChoice)))
        validChoice = True
    else:
        print('Invalid item. Please try again!')
