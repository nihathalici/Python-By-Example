
'''
AS-047
Ask the user to enter a number and then enter another number.
Add these two numbers together and then ask if they want
to add another number. If they enter "y", ask them to enter
another number and keep adding numbers until they do not
answer "y". Once the loop has stopped, display the total.
'''

#####
# Python By Example
# Exercise 047
# Christopher Hagan
#####

firstNum = int(input('Enter the first number to be added together: '))
total = firstNum
addAnother = 'y'

while addAnother.lower().startswith('y'):
    additionalNum = int(input('Enter the next number to add: '))
    total += additionalNum
    addAnother = input('Would you like to add another number to the total: ')

print('The final total of these numbers is {}'.format(total))
    
