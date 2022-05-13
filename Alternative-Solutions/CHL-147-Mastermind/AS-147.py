"""
AS-147
Mastermind:
You are going to make an on-screen version of the board game 
“Mastermind”.
"""
#####
# Python By Example
# Exercise 147
# Christopher Hagan
#####

import random

listOfPossibleColours = ['Red', 'Green', 'Blue', 'Orange']

def generateComputerSequence():
    computerSequence = []
    for i in range(0, 4):
        computerSequence.append(random.choice(listOfPossibleColours))
    
    return computerSequence


def guessSequence():
    print('\n---\nMake a guess\nYou may enter simply the first letter of each colour\nSeparate each colour by a space\n---\n')
    validGuess = False
    while validGuess == False:
        userGuess = input('My guess is: ')
        newGuess = []
        for colour in userGuess.split():
            for possibleColour in listOfPossibleColours:
                if colour.lower().startswith(possibleColour[0].lower()):
                    newGuess.append(possibleColour)

        if len(newGuess) == 4:
            validGuess = True
        else:
            print('\n***This guess was not valid, please try again!\nAn example guess would be Orange Red Red Blue\n***\n')

    return newGuess


def checkGuessAgainstSequence(userGuess, correctSequence):
    correctPlace = wrongPlace = 0
    coloursNotInTheCorrectSequence = []
    for i in range(0, len(userGuess)):
        if userGuess[i] == correctSequence[i]:
            correctPlace += 1
        else:
            for j in range(0, len(correctSequence)):
                if ((userGuess[i] == correctSequence[j]) and (userGuess[j] != correctSequence[j])):
                    wrongPlace += 1
            
    return correctPlace, wrongPlace


numberOfuserGuesses = 0
correctSequence = generateComputerSequence()

print("""\n\n===========\nMastermind\n===========
**********\nThe Computer has randomly selected 4 colours in a specific sequence.
You must try to guess that sequence.
You may choose from the following list of colours {}, {}, {} and {}.
Keep in mind that the computer can choose the same colour multiple times in the sequence!\n**********""".format(listOfPossibleColours[0],
    listOfPossibleColours[1], listOfPossibleColours[2], listOfPossibleColours[3]))

guessAgain = True
while (guessAgain):
    numberOfuserGuesses += 1
    guess = guessSequence()

    print(correctSequence)

    print('\n-----\nYour guess was {}, {}, {}, {}'.format(guess[0],guess[1],guess[2],guess[3]))
    correctPlace, wrongPlace = checkGuessAgainstSequence(guess, correctSequence)
    if (correctPlace == len(correctSequence)):
        print('Congratulations you guessed correctly, you managed to win in {} guesses.'.format(numberOfuserGuesses))
        guessAgain = False
    else:
        print('\nCorrect colour in the correct place : {}\nCorrect colour in the wrong place : {}'.format(correctPlace, wrongPlace))

print('Game over!')
