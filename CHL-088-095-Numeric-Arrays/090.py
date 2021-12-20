'''
Ask the user to enter numbers. If they enter a number between 10 and 20,
save it in the array, otherwise display the message “Outside the range”.
Once five numbers have been successfully added, display the message “Thank you”
and display the array with each item shown on a separate line.
'''

from array import *

nums = array('i', [])

while len(nums) < 5:
    num = int(input("Enter a number between 10 and 20: "))
    if num >= 10 and num <= 20:
        nums.append(num)
    else:
        print("Outside the range")

for i in nums:
    print(i)
    
