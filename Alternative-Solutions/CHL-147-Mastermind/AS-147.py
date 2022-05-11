"""
AS-147
Mastermind:
You are going to make an on-screen version of the board game 
“Mastermind”.
"""

import random

def select_col():
    colours = ["r", "b", "o", "y", "p", "g", "w"]
    c1 = random.choice(colours)
    c2 = random.choice(colours)
    c3 = random.choice(colours)
    c4 = random.choice(colours)
    data = (c1, c2, c3, c4)

def tryit(c1, c2, c3, c4):
    pass

def main():
    (c1, c2, c3, c4) = select_col()
    score = 0
    play = True
    while play == True:
        (correct, wrong_place) = tryit(c1, c2, c3, c4)
        score += 1
        if correct  == 4:
            play = False
    print("You win!")
    print("You took", score, "guesses")
    

main()
