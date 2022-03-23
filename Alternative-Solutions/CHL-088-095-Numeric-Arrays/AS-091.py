'''
AS-091
Create an array which contains five numbers (two of which should be repeated).
Display the whole array to the user. Ask the user to enter one of the
numbers from the array and then display a message saying how many times that number
appears in the list.
'''
#####
# Python By Example
# Exercise 091
# Christopher Hagan
#####

from array import *

nums = array('i', [15, 18, 58, 94, 58])
print(nums)
userChoice = int(input('Enter a number to query: '))

# count = 0
# for i in nums:
#     if i == userChoice:
#         count += 1

print('The number you queried exists {} time(s) in the list.'.format(nums.count(userChoice)))
