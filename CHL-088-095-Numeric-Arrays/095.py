'''
Create an array of five numbers between 10 and 100 which each have
two decimal places. Ask the user to enter a whole number between 2 and 5.
If they enter something outside of that range, display a suitable error message
and ask them to try again until they enter a valid amount. Divide each of the
numbers in the array by the number the user entered and display the answers
shown to two decimal places.
'''

from array import *
import math

nums = array('f', [34.75, 27.23, 99.58, 45.26, 28.65])
tryagain = True
while tryagain == True:
    num = int(input("Enter a number between 2 and 5: "))
    if num < 2 or num > 5:
        print("Incorrect value, try again.")
    else:
        tryagain = False

for i in range(0, 5):
    ans = nums[i]/num
    print(round(ans, 2))
