'''
Create an array which contains five numbers (two of which should be repeated).
Display the whole array to the user. Ask the user to enter one of the
numbers from the array and then display a message saying how many times that number
appears in the list.
'''

from array import *

myArray = array('i', [2, 3, 5, 8, 5])

print(myArray)

inp = int(input("Enter a number: "))

print(myArray.count(inp))

'''
Author's solution:

nums = array('i', [5, 7, 9, 2, 9])

for i in nums:
    print(i)

num = int(input("Enter a number: "))

if nums.count(num) == 1:
    print(num, "is in the list once")
else:
    print(num, "is in the list", nums.count(num), "times")
'''
