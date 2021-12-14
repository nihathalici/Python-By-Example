'''
Randomly pick a whole number between 1 and 10. Ask the user to enter a number
and keep entering numbers until they enter the number that was randomly picked.
'''


import random

rd_ch = random.randint(1,10)
us_ch = int(input("Pick a number"))
while rd_ch != us_ch:
    
    if rd_ch == us_ch:
        print("Correct")
    else:
        us_ch = int(input("Try Pick another number"))

if rd_ch == us_ch:
    print("Well done!")
else:
    if rd_ch > us_ch:
        us_ch = int(input("You are too too low. Pick a second number"))
    elif rd_ch < us_ch:
        us_ch = int(input("You are too too high. Pick a second number"))
        if us_ch == rd_ch:
            print("Correct!")
            else:
        print("You lose!")
    
