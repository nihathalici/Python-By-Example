'''
Create two arrays (one containing three numbers that the user enters and one
containing a set of five random numbers).

Join these two arrays together into one large array. Sort this large array
and display it so that each number appears on a separate line.
'''

from array import *
import random

firstArray = array('i', [])
secondArray = array('i', [])

while len(firstArray) < 3:
    num = int(input("Enter num: "))
    firstArray.append(num)

for x in range(5):
    num = random.randint(10, 30)
    secondArray.append(num)

largeArray = sorted(firstArray + secondArray)

for item in largeArray:
    print(item)
