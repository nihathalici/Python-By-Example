'''
Display an array of five numbers. Ask the user to select one of the numbers.
Once they have selected a number, display the position of that item in the
array. If they enter something that is not in the array, ask them to try
again until they select a relevant item.
'''

from array import *

nums = array('i', [2, 5, 7, 9, 13])
print(nums)
inp = int(input("Enter a number: "))

while inp not in nums:
    print("Try again: ")
    inp = int(input("Enter a number: "))
print("The number {} has the index {} on the list.".format(inp, nums.index(inp)))


'''
Author's solution:

nums = array('i', [4, 6, 8, 2, 5])

for i in nums:
    print(i)

num = int(input("Select one of the numbers: "))

tryagain = True
while tryagain == True:
    if num in nums:
        print("This is in position", nums.index(num))
        tryagain = False
    else:
        print("Not in array")
        num = int(input("Select one of the numbers: "))
    
    

