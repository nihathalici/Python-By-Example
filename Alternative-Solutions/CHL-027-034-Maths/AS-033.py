'''
AS-033
Ask the user to enter two numbers. Use whole number division to divide
the first number by the second and also work out the remainder and
display the answer in a user-friendly way
(e.g. if they enter 7 and 2 display “7 divided by 2 is 3 with 1 remaining”).
'''

#####
# Python By Example
# Exercise 033
# Christopher Hagan
#####

numerator = int(input('Enter a whole number as the numerator: '))
denominator = int(input('Enter another whole number which will be the denominator: '))
print('{} divided by {} is {} with {} remaining.'.format(numerator, denominator, (numerator // denominator), (numerator % denominator)))

