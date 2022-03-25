'''
AS-093
Ask the user to enter five numbers. Sort them into order and present them
to the user. Ask them to select one of the numbers. Remove it from the
original array and save it in a new array.
'''

#####
# Python By Example
# Exercise 093
# Christopher Hagan
#####

from array import *

nums = array('i', [])
removedNums = array('i', [])

while len(nums) < 5:
    newNum = int(input('Enter a number to append to the array: '))
    nums.append(newNum)

nums = sorted(nums)
print(nums)

userChoice = int(input('Enter a number to move to the new array: '))
nums.remove(userChoice)
removedNums.append(userChoice)

print(nums)
print(removedNums)





