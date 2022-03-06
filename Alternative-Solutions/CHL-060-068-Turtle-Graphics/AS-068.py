'''
AS-068
Draw a pattern that will change each time the program is run.
Use the random function to pick the number of lines, the length
of each line and the angle of each turn.
'''

#####
# Python By Example
# Exercise 068
# Christopher Hagan
#####

import turtle, random

randomShape = random.randint(4, 12)
randomLines = random.randint(1, 20)
shapeSide = random.randrange(50, 200, 10)

for i in range(0, randomLines):
    turtle.left(int(360/randomLines))
    for j in range(0, randomShape):
        turtle.forward(shapeSide)
        turtle.left(int(360 / randomShape))

turtle.exitonclick()


