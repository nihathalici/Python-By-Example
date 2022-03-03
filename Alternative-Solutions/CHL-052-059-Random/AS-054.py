'''
AS-054
Randomly choose either heads or tails (“h” or “t”). Ask the user to make
their choice. If their choice is the same as the randomly selected value,
display the message “You win”, otherwise display “Bad luck”.
At the end, tell the user if the computer selected heads or tails.
'''

#####
# Python By Example
# Exercise 054
# Christopher Hagan
#####

import random

coinFlip = random.choice(['Heads', 'Tails'])
userGuess = input('The computer has flipped a coin, guess whether it was heads of tails (h or t): ')

if userGuess.lower() == coinFlip[0].lower():
    print('\nYou guessed correctly!')
else:
    print('\nYour guess was wrong!')

print('\nThe result of the computer flipping a coin was {}\n'.format(coinFlip))















