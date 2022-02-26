
'''
AS-049
Create a variable called compnum and set the value to 50. Ask the user to enter a number.
While their guess is not the same as the compnum value, tell them if their guess is too
low or too high and ask them to have another guess. If they enter the same value as
compnum, display the message “Well done, you took [count] attempts”.
'''

#####
# Python By Example
# Exercise 049
# Christopher Hagan
#####

compnum = 50
guess = count = 0

while guess != compnum:
    guess = int(input('Try to guess the hidden number: '))
    if guess < compnum:
        print('Your guess was too low! Please have another guess.')
    elif guess > compnum:
        print('Your guess was too high! Please have another guess.')
    count += 1

print('Well done it took you {} guesses'.format(count))
