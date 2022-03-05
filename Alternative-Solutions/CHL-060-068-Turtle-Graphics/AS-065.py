'''
AS-065
Write the numbers as shown below,
starting at the bottom of the number one.
123
'''

#####
# Python By Example
# Exercise 065
# Christopher Hagan
#####

import turtle

numberHeight = 150
numberWidth = 100
maxNumbers = 3

for i in range(0, maxNumbers):
    if i == 0:
        turtle.left(90)
        turtle.forward(numberHeight)
        turtle.right(90)
    if i == 1:
        turtle.forward(numberWidth)
        turtle.right(90)
        turtle.forward(int(numberHeight/2))
        turtle.right(90)
        turtle.forward(numberWidth)
        turtle.left(90)
        turtle.forward(int(numberHeight/2))
        turtle.left(90)
        turtle.forward(numberWidth)
    if i == 2:
        turtle.forward(numberWidth)
        turtle.left(90)
        turtle.forward(int(numberHeight/2))
        turtle.left(90)
        turtle.forward(numberWidth)
        turtle.left(180)
        turtle.forward(numberWidth)
        turtle.left(90)
        turtle.forward(int(numberHeight/2))
        turtle.left(90)
        turtle.forward(numberWidth)

    if i < (maxNumbers-1):
        turtle.penup()
        turtle.forward(numberWidth*2)
        turtle.pendown()

turtle.exitonclick()
