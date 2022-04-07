'''
AS-119
Define a subprogram that will ask the user to pick a low and a high
number, and then generate a random number between those two values and store
it in a variable called “comp_num”.

Define another subprogram that will give the instruction “I am thinking of
a number...” and then ask the user to guess the number they are thinking of.

Define a third subprogram that will check to see if the comp_num is the same
as the user’s guess. If it is, it should display the message “Correct, you
win”, otherwise it should keep looping, telling the user if they are too low
or too high and asking them to guess again until they guess correctly.
'''

#####
# Python By Example
# Exercise 119
# Christopher Hagan
#####

import random

def generateRandomNumber():
    low = int(input('Enter the lower boundary for a random number: '))
    high = int(input('Enter the higher boundary for a random number: '))
    comp_num = random.randint(low, high)
    return comp_num

def guessNumber():
    print('I am thinking of a number...')
    userGuess = int(input('What number am I thinking of: '))
    return userGuess

def main():
    correctGuess = False
    randomNumber = generateRandomNumber()
    while not correctGuess:
        guess = guessNumber()
        if randomNumber == guess:
            print('Correct, you win!')
            correctGuess = True
        else:
            if guess < randomNumber:
                print('Too Low')
            else:
                print('Too High')
            print('Guess Again!')

main()
