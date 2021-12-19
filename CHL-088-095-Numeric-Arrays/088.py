'''
Ask the user for a list of five integers.
Store them in an array. Sort the list and display it in reverse order.
'''
from array import *

myArray = array('i', [])
cnt = 5
for item in range(0, cnt):
    val = int(input("Enter num: "))
    myArray.append(val)

myArray = sorted(myArray)

myArray.reverse()

print(myArray)
