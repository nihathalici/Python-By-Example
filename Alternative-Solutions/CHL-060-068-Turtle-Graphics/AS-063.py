'''
AS-063
Draw three squares in a row with a gap between each.
Fill them using three different colours.
'''

#####
# Python By Example
# Exercise 063
# Christopher Hagan
#####

import turtle

sizeOfSquare = 100

for i in range(0, 3):
    turtle.begin_fill()
    if i == 0:
        turtle.color('black', 'red')
    elif i > 0:
        turtle.penup()
        turtle.forward(sizeOfSquare * 2)
        turtle.pendown()
        if i == 1:
            turtle.color('black', 'purple')
        if i == 2:
            turtle.color('black', 'green')
    for j in range(0, 4):
        turtle.forward(sizeOfSquare)
        turtle.right(90)
    turtle.end_fill()

turtle.exitonclick()











