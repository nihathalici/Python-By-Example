'''
AS-088
Ask the user for a list of five integers.
Store them in an array. Sort the list and display it in reverse order.
'''
#####
# Python By Example
# Exercise 088
# Christopher Hagan
#####

from array import *

nums = array('i', [])
for i in range(0, 5):
    newNum = int(input('Enter a number: '))
    nums.append(newNum)

nums = sorted(nums)
nums.reverse()
print(nums)






