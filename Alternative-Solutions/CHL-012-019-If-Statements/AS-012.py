'''
AS-012
Ask for two numbers. If the first one is larger than the second, display
the second number first and then the first number, otherwise show the first
number first and then the second.
'''

#####
# Python By Example
# Exercise 012
# Christopher Hagan
#####

firstNum = int(input('Please enter your first number: '))
secondNum = int(input('Please enter your second number: '))

if firstNum > secondNum:
    print('{}, {}'.format(secondNum, firstNum))
else:
    print('{}, {}'.format(firstNum, secondNum))
