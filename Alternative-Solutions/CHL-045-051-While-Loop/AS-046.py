
'''
AS-046
Ask the user to enter a number. Keep asking until they enter a value over 5
and then display the message "The last number you entered was a [number]"
and stop the program.
'''

#####
# Python By Example
# Exercise 046
# Christopher Hagan
#####

num = 0

while num < 5:
    num = int(input('Enter a number: '))

print('The last number entered was {}'.format(num))
