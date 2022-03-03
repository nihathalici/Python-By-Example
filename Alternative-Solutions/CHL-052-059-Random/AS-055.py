'''
AS-055
Randomly choose a number between 1 and 5. Ask the user to pick a number.
If they guess correctly, display the message “Well done”, otherwise tell
them if they are too high or too low and ask them to pick a second number.
If they guess correctly on their second guess, display “Correct”, otherwise
display “You lose”.
'''

#####
# Python By Example
# Exercise 055
# Christopher Hagan
#####

import random

randomNumber = random.randint(1, 5)
userGuess = int(input('Guess the random number between 1 and 5: '))
if userGuess == randomNumber:
    print('Well done!')
else:
    if userGuess < randomNumber:
        print('Too low!')
    else:
        print('Too high!')
    userGuess = int(input(Guess again: ))
    if userGuess == randomNumber:
        print('Correct!')
    else:
        print('You lose!')





























