'''
AS-120
Display the following menu to the user:
    1) Addition
    2) Subtraction
    Enter 1 or 2:

If they enter a 1, it should run a subprogram that will
generate two random numbers between 5 and 20, and
ask the user to add them together. Work out the correct
answer and return both the user’s answer and the
correct answer.

If they entered 2 as their selection on the menu, it
should run a subprogram that will generate one number
between 25 and 50 and another number between 1 and
25 and ask them to work out num1 minus num2. This
way they will not have to worry about negative answers.
Return both the user’s answer and the correct answer.

Create another subprogram that will check if the user’s
answer matches the actual answer. If it does, display
“Correct”, otherwise display a message that will say
“Incorrect, the answer is” and display the real answer.

If they do not select a relevant option on the first menu
you should display a suitable message.
'''

#####
# Python By Example
# Exercise 120
# Christopher Hagan
#####

import random

def menu():
    validOptionSelected = False
    while not validOptionSelected:
        print('----------')
        print('1) Addition')
        print('2) Subtraction')
        print('----------')
        selection = input('Enter 1 or 2: ')
        print('----------')
        if selection in ('1', '2'):
            validOptionSelected = True
        else:
            print('Not allowed, please try again...')
    
    return selection

def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    userGuess = int(input('What is {} + {}'.format(num1, num2)))
    actualAnswer = num1 + num2
    return (userGuess, actualAnswer)

def subtraction():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    userGuess = int(input('What is {} - {} ='.format(num1, num2)))
    actualAnswer = num1 - num2
    return(userGuess, actualAnswer)

def checkAnswer(userGuess, actualAnswer):
    if userGuess == actualAnswer:
        print('Correct')
    else:
        print('Incorrect, the answer is {}'.format(actualAnswer))

def main():
    selection = menu()
    if selection == '1':
        userGuess, actualAnswer = addition()
    else:
        userGuess, actualAnswer = subtraction()
    checkAnswer(userGuess, actualAnswer)

main()