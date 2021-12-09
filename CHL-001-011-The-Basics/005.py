'''
Ask the user to enter three numbers. Add together the first two numbers and then multiply
this total by the third. Display the answer as

The answer is [answer].
'''

num1 = int(input('Enter the first number.'))
num2 = int(input('Enter the second number.'))
num3 = int(input('Enter the third number.'))

print('The answer is', ((num1 + num2) * num3))

'''
Author's solution:

num1 = int(input('Please enter your first number: '))
num2 = int(input('Please enter your second number: '))
num3 = int(input('Please enter your third number: '))
answer = (num1 + num2)* num3
print("The answer is", answer)
'''

