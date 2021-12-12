'''
Ask the user to enter an integer that is over 500. Work out the
square root of that number and display it to two decimal places.
'''
import math

num = int(input('Enter an integer that is over 500: '))
print(round((math.sqrt(num)), 2))
