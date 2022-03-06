'''
AS-062
Draw a circle.
'''

#####
# Python By Example
# Exercise 062
# Christopher Hagan
#####

import turtle

steps = 1

for i in range(0, int(360/steps)):
    turtle.forward(steps)
    turtle.right(steps)

turtle.exitonclick()

