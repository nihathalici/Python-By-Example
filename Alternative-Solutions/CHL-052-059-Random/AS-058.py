'''
AS-058
Make a maths quiz that asks five questions by randomly generating two whole
numbers to make the question (e.g. [num1] + [num2]). Ask the user to enter
the answer. If they get it right add a point to their score. At the end of
the quiz, tell them how many they got correct out of five.
'''

#####
# Python By Example
# Exercise 058
# Christopher Hagan
#####

import random

correctAnswers = 0
maxQuestions = 5
for i in range(0, maxQuestions):
    firstNumber = random.randint(1, 100)
    secondNumber = random.randint(1, 100)
    userGuess = int(input('What is {} + {} : '.format(firstNumber, secondNumber)))
    if userGuess == (firstNumber + secondNumber):
        correctAnswers += 1

print('\nYou got {} correct out of {}.\n'.format(correctAnswers, maxQuestions))
    
