'''
AS-089
Create an array which will store a list of integers. Generate five random
numbers and store them in the array. Display the array (showing each
item on a separate line).
'''

#####
# Python By Example
# Exercise 089
# Christopher Hagan
#####

from array import *
import random

nums = array('i', [])
for i in range(0, 5):
    nums.append(random.randint(0, 999))

for i in nums:
    print(i)
