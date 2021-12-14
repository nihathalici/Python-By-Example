'''
Randomly choose either heads or tails (“h” or “t”). Ask the user to make
their choice. If their choice is the same as the randomly selected value,
display the message “You win”, otherwise display “Bad luck”.
At the end, tell the user if the computer selected heads or tails.
'''
import random



rd_ch = random.choice(['h', 't'])
us_ch = input("Make your choice (h/t)")
if rd_ch == us_ch:
    print("You win!")
else:
    print("Bad luck. It was, ", rd_ch)
    
