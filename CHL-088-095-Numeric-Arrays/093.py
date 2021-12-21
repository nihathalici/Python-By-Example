'''
Ask the user to enter five numbers. Sort them into order and present them
to the user. Ask them to select one of the numbers. Remove it from the
original array and save it in a new array.
'''

from array import *

nums = array('i', [])

for i in range(0, 5):
    num = int(input("Enter a number: "))
    nums.append(num)

nums = sorted(nums)

for i in nums:
    print(i)

num = int(input("Select a number from the array: "))
if num in nums:
    nums.remove(num)
    num2 = array('i', [])
    num2.append(num)
    print(nums)
    print(num2)
else:
    print("That is not a value in the array")

