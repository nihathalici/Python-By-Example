'''
Create an array which will store a list of integers. Generate five random
numbers and store them in the array. Display the array (showing each
item on a separate line).
'''
import random
from array import *

newArray = array('i', [])

for i in range(0, 5):
    num = random.randint(1, 50)
    newArray.append(num)

for item in newArray:
    print(item)
