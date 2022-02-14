'''
Ask the user to enter three numbers. Add together the first two numbers and then multiply
this total by the third. Display the answer as

The answer is [answer].
'''

#####
# Python By Example
# Exercise 005
# Christopher Hagan
#####

firstNumber = int(input('Enter your first number: '))

secondNumber = int(input('Enter a second number to add to the first number: '))

thirdNumber = int(input('Enter a third number to multiply the total of the first and second numbers by: '))

print('The answer is {}'.format((firstNumber + secondNumber) * thirdNumber))
