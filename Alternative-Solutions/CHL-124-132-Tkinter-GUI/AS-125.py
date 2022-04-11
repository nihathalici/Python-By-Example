'''
AS-125
Write a program that can be used instead of rolling a six-sided
die in a board game. When the user clicks a button it should
display a random whole number between 1 to 6 (inclusive).
'''
# Python By Example
# Exercise 124
# Christopher Hagan
#####

from tkinter import *
import random
from unittest import result

def rollDice():
    roll = random.randint(1, 6)
    result['text'] = 'You got a {}'.format(roll)

window = Tk()
window.geometry("300x200")
window.title('Rolling a dice')

button = Button(text = 'Roll Dice', command = rollDice)
button.place(x=50, y=50, width=100, height=50)

result = Message(text='')
result.place(x=50, y=125, width=100, height=50)

window.mainloop()

