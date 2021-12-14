'''
Randomly choose a number between 1 and 5. Ask the user to pick a number.
If they guess correctly, display the message “Well done”, otherwise tell
them if they are too high or too low and ask them to pick a second number.
If they guess correctly on their second guess, display “Correct”, otherwise
display “You lose”.
'''

import random

rd_ch = random.randint(1,5)
us_ch = int(input("Pick a number"))
if rd_ch == us_ch:
    print("Well done!")
else:
    us_ch = int(input("You are too high or too low. Pick a second number"))
    if us_ch == rd_ch:
        print("Correct!")
    else:
        print("You lose!")
    
