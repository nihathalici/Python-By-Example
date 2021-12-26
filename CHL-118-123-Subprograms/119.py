'''
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
import random

def pick_num():
    low = int(input("Enter the bottom of the range: "))
    high = int(input("Enter the top of the range: "))
    comp_num = random.randint(low, high)
    return comp_num

def first_guess():
    print("I am thinking of a number...")
    guess = int(input("What am I thinking of: "))
    return guess

def check_answer(comp_num, guess):
    try_again = True
    while try_again == True:
        if comp_num == guess:
            print("Correct, you win.")
            try_again = False
        elif comp_num > guess:
            guess = int(input("Too low, try again: "))
        else:
            guess = int(input("Too high, try again: "))

def main():
    comp_num = pick_num()
    guess = first_guess()
    check_answer(comp_num, guess)

main()
