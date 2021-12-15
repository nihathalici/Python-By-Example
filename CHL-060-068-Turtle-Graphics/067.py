'''
Create the following pattern:
'''

import turtle

for x in range(0, 10):
    for i in range(0, 8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.hideturtle()

turtle.exitonclick()
